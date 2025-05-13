from collections import defaultdict

from dateutil import parser
from sqlalchemy.orm import sessionmaker

from uaclient.config.clientConfig import device, collect_buff_size
from uaclient.config.mysqlConfig import engine
from uaclient.db_entity.deviceNodeData import DeviceNodeData
from uaclient.db_entity.deviceNode import DeviceNode


def save2database(func):
    def wrapper(self, *args):
        device_upload(*args)
        return func(self, *args)

    return wrapper


_buffer = defaultdict(list)


def device_upload(node, value, timestamp):
    stack = _buffer[node]
    stack.append((value, timestamp))
    if len(stack) > collect_buff_size:
        stack.pop(0)
    # print(f"节点: {node}, 数据条数: {len(stack)}")


def save_to_database():
    _do_save()
    # max_worker_num = math.floor(len(buffer.items()) / 5)
    # if max_worker_num < 1:
    #     max_worker_num = 3
    # with ThreadPoolExecutor(max_workers=max_worker_num) as executor:
    #     executor.submit(_do_save)


def _do_save():
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
                    created_at=parser.parse(time_str)
                ))
        if data_list:
            # print(f"保存数据到数据库，条数: {len(data_list)}")
            s.add_all(data_list)
            s.commit()


def group_nodes():
    _do_group()


def _do_group():
    session = sessionmaker(bind=engine)
    with session() as s:
        results = [row[0] for row in s.query(DeviceNodeData.node).group_by(DeviceNodeData.node).all()]
        if len(results) > 0:
            existed_nodes = {row[0] for row in s.query(DeviceNode.node).filter(DeviceNode.node.in_(results))}
            new_nodes = [item for item in results if item not in existed_nodes]
            nodes = []
            if len(new_nodes) > 0:
                for node in new_nodes:
                    nodes.append(DeviceNode(
                        device=device['name'],
                        node=str(node),
                    ))
            if len(nodes) > 0:
                s.add_all(nodes)
                s.commit()
