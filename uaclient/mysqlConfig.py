from sqlalchemy import create_engine

db_config = {
    'db_host': '127.0.0.1',
    'db_port': '3306',
    'db_user': 'root',
    'db_password': 'pjdgul2k',
    'db_name': 'opcua_client_persist_test'
}
db_url = f'mysql+pymysql://{db_config["db_user"]}:{db_config["db_password"]}@{db_config["db_host"]}:{db_config["db_port"]}/{db_config["db_name"]}'
engine = create_engine(
    db_url,
    pool_size=30,  # 连接池大小
    max_overflow=60,  # 最大溢出连接数
    pool_timeout=30,  # 连接池超时时间
    echo=False,
    connect_args={
        'charset': 'utf8mb4',
        'collation': 'utf8mb4_unicode_ci',
        'max_allowed_packet': 1024 * 1024 * 200,  # 最大包大小
        'init_command': 'SET time_zone = "+08:00"',
        'sql_mode': 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'
    }
)
is_connected = False
try:
    if engine is None:
        raise "创建数据库连接失败！"
    try:
        engine.connect()
        is_connected = True
    except Exception as e:
        raise "数据库连接失败，请检查参数！"
except Exception as e:
    pass

print("--------------------------------")
print(engine)
print("--------------------------------")
