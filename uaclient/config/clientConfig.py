import argparse

app_name = 'opcua client'

_parser = argparse.ArgumentParser()

_parser.add_argument('--debug', action='store_true', default=False)

# 设备号（存储数据时必须）
_parser.add_argument('--device', type=str, required=True)

# 数据库相关配置
_parser.add_argument('--standalone', action='store_true', default=False)  # 开启这项将使用 SQLite 数据库
_parser.add_argument('--db_host', default='localhost')
_parser.add_argument('--db_port', default=3306)
_parser.add_argument('--db_user', default='root')
_parser.add_argument('--db_password', default='pjdgul2k')
_parser.add_argument('--db_name', default='data')

# 采集相关配置
_parser.add_argument('--collect_enabled', action='store_true', default=True)
_parser.add_argument('--collect_buff_size', type=int, default=5)
_parser.add_argument('--collect_freq_sec', type=int, default=3)

_args = _parser.parse_args()

# 是否为调试模式
debug_mode = _args.debug

# 设备号
device = _args.device

# 是否是独立运行（使用SQLite）
db_standalone = _args.standalone

db_config = {
    'db_host': _args.db_host,
    'db_port': _args.db_port,
    'db_user': _args.db_user,
    'db_password': _args.db_password,
    'db_name': _args.db_name
}

# 采集频率和采集 buff 大小
collect_enabled = _args.collect_enabled
collect_buff_size = _args.collect_buff_size
if collect_buff_size < 1:
    collect_buff_size = 5
collect_freq_sec = _args.collect_freq_sec
if collect_freq_sec < 1:
    collect_freq_sec: 1
