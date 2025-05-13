from sqlalchemy import Column, Integer, String, Text, DateTime

from . import Base


class DeviceNodeData(Base):
    """
    【设备节点数据表】实体类
    """

    __tablename__ = 'device_node_data'

    id = Column(Integer, primary_key=True, nullable=False)
    device = Column(String(50), nullable=False, comment='设备')
    node = Column(String(300), nullable=False, comment='节点')
    data = Column(Text(500), nullable=False, comment='数据')
    created_at = Column(DateTime, nullable=False, comment='时间')
