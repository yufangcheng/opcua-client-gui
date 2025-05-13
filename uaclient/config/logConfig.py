import logging

from uaclient.config.clientConfig import app_name

logger = logging.getLogger(__name__)

# 创建一个文件处理器
file_handler = logging.FileHandler(f'{app_name}.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)
