import traceback

from sqlalchemy import create_engine

from uaclient.config.clientConfig import debug_mode, db_standalone, db_config
from uaclient.config.logConfig import logger

"""
以下数据库实体类导入【不要删除！！！】
这里 import 是为了让数据库实体类在初始化时被注册到 Base 中
在 standalone 模式下，使用 SQLite 数据库，启动后使用 Base.metadata.create_all() 创建表
"""
from uaclient.db_entity.deviceNodeData import DeviceNodeData
from uaclient.db_entity.deviceNodeData2 import DeviceNodeData2
from uaclient.db_entity.deviceNode import DeviceNode

"""
该目录模块中的 __init__.py 执行了 Base = declarative_base()
用以注册上面导入的实体类
"""
from uaclient.db_entity import Base

engine = None
if db_standalone:
    engine = create_engine(
        f'sqlite:///{db_config["db_name"]}.db',
        pool_size=30,  # 连接池大小
        max_overflow=60,  # 最大溢出连接数
        pool_timeout=30,  # 连接池超时时间
        echo=debug_mode,
    )
else:
    db_url = f'mysql+pymysql://{db_config["db_user"]}:{db_config["db_password"]}@{db_config["db_host"]}:{db_config["db_port"]}/{db_config["db_name"]}'
    engine = create_engine(
        db_url,
        pool_size=30,  # 连接池大小
        max_overflow=60,  # 最大溢出连接数
        pool_timeout=30,  # 连接池超时时间
        echo=debug_mode,
        connect_args={
            'charset': 'utf8mb4',
            'collation': 'utf8mb4_unicode_ci',
            'max_allowed_packet': 1024 * 1024 * 200,  # 最大包大小
            'init_command': 'SET time_zone = "+08:00"',
            'sql_mode': 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'
        }
    )
if engine is None:
    logger.error(f"异常调用栈: {traceback.format_exc()}")
    raise "创建数据库连接失败！"
try:
    engine.connect()
except Exception as e:
    logger.error(f"异常调用栈: {traceback.format_exc()}")
    raise "数据库连接失败，请检查参数！"

print("--------------------------------")
print(f"Standalone: {db_standalone}")
print(engine)
print("--------------------------------")

# 如果用 SQLite 则用所有实体类初始化数据库
if db_standalone:
    print(f"初始化数据库: {engine}")
    Base.metadata.create_all(engine, checkfirst=True)
