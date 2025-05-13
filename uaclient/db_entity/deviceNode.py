from sqlalchemy import Column, Integer, String, Text, DateTime

from . import Base


class DeviceNode(Base):
    """
    【设备节点表】实体类
    """

    __tablename__ = 'device_nodes'

    id = Column(Integer, primary_key=True, nullable=False)
    device = Column(String(50), nullable=False, comment='设备')
    node = Column(String(300), nullable=False, comment='节点')
    node_name = Column(String(300), nullable=True, comment='节点名称')
