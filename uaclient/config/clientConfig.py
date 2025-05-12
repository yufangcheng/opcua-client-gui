import argparse

app_name = 'opcua client'

parser = argparse.ArgumentParser()

parser.add_argument('--debug', action='store_true', default=False)

# 数据库相关配置
parser.add_argument('--standalone', action='store_true', default=False)  # 开启这项将使用 SQLite 数据库
parser.add_argument('--db_host', default='localhost')
parser.add_argument('--db_port', default=3306)
parser.add_argument('--db_user', default='root')
parser.add_argument('--db_password', default='pjdgul2k')
parser.add_argument('--db_name', default='data')

# 采集相关配置
parser.add_argument('--collect_enabled', action='store_true', default=True)
parser.add_argument('--collect_buff_size', default=5)
parser.add_argument('--collect_freq_sec', default=3)

args = parser.parse_args()

# 是否为调试模式
debug_mode = args.debug
db_standalone = args.standalone

db_config = {
    'db_host': args.db_host,
    'db_port': args.db_port,
    'db_user': args.db_user,
    'db_password': args.db_password,
    'db_name': args.db_name
}

# 采集频率和采集 buff 大小
collect_enabled = args.collect_enabled
collect_buff_size = args.collect_buff_size
if collect_buff_size < 0:
    collect_buff_size = 5
collect_freq_sec = args.collect_freq_sec
if collect_freq_sec < 1:
    collect_freq_sec: 2
