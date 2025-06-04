import csv
import json
import os
from collections import defaultdict
from datetime import datetime

from dateutil import parser
from sqlalchemy.orm import sessionmaker

from uaclient.config.clientConfig import device, collect_buff_size
from uaclient.config.mysqlConfig import engine
from uaclient.db_entity.deviceNodeData import DeviceNodeData
from uaclient.db_entity.deviceNodeData2 import DeviceNodeData2


def save2database(func):
    """
    使用该装饰器可以将采集数据压入内存栈
    """

    def wrapper(self, *args):
        device_upload(*args)
        return func(self, *args)

    return wrapper


_buffer = defaultdict(list)


def device_upload(node, value, timestamp):
    """
    将采集数据压入内存栈中，最多 collect_buff_size 个
    """
    stack = _buffer[node]
    stack.append((value, timestamp))
    if len(stack) > collect_buff_size:
        stack.pop(0)
    # print(f"节点: {node}, 数据条数: {len(stack)}")


def save_to_database_from_stack():
    """
    从内存栈中读取数据并保存到数据库
    """
    session = sessionmaker(bind=engine)
    with session() as s:
        data_list = []
        buffer_copy = _buffer.copy()
        _buffer.clear()
        for node, data_stack in buffer_copy.items():
            # print(f"处理节点: {node}, 数据: {data_stack}")
            if data_stack:
                data, time_str = data_stack.pop()
                data_list.append(DeviceNodeData(
                    device=device['name'],
                    node=str(node),
                    data=str(data),
                    data_report_at=parser.parse(time_str),
                    created_at=datetime.now()
                ))
        if data_list:
            # print(f"保存数据到数据库，条数: {len(data_list)}")
            s.add_all(data_list)
            s.commit()


def save_to_database_from_reading_nodes(subscribed_nodes):
    """
    读取订阅节点的数据并保存到数据库
    """
    if len(subscribed_nodes) > 0:
        session = sessionmaker(bind=engine)
        with session() as s:
            data = {}
            data_list = []
            headers = ['机台编号', '采集时间']
            source_datetime = None
            for node in subscribed_nodes:
                display_name = node.read_display_name().Text
                headers.append(display_name)
                node_value = node.read_value()
                data_list.append(node_value)
                data[node.nodeid.to_string()] = node_value
                if source_datetime is None:
                    source_datetime = node.get_data_value().SourceTimestamp

            rows = [
                device['name'],
                int(source_datetime.timestamp())
            ]
            rows.extend(data_list)
            save_to_csv(headers, rows, f"{device['name']}_{datetime.now().strftime('%Y%m%d')}.csv")

            s.add(DeviceNodeData2(
                device=device['name'],
                data=str(json.dumps(data, ensure_ascii=False)),
                data_report_at=int(source_datetime.timestamp()),
                created_at=int(datetime.now().timestamp())
            ))
            s.commit()


def save_to_csv(headers, data, file_path):
    if not headers:
        return
    if not file_path:
        print("保存位置不能为空")
        return
    # 检查文件是否存在
    file_exists = os.path.exists(file_path)

    try:
        # 使用 'a' 模式打开文件以追加内容，设置 newline='' 避免 Windows 平台行末多出空行
        with open(file_path, 'a', newline='', encoding='GB2312') as csvfile:
            # 创建 CSV 写入器对象
            writer = csv.writer(csvfile)

            # 如果文件不存在，写入列名
            if not file_exists:
                writer.writerow(headers)

            # 写入多行数据
            writer.writerows([data])

        action = "创建" if not file_exists else "追加"
        print(f"CSV 文件已成功{action}：{file_path}")

    except Exception as e:
        print(f"处理 CSV 文件时出错：{e}")
