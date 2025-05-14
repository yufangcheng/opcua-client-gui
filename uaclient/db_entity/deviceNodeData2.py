from sqlalchemy import Column, Integer, String, Text, DateTime

from . import Base


class DeviceNodeData2(Base):
    """
    【设备节点数据表】实体类
    """

    __tablename__ = 'device_node_data2'

    id = Column(Integer, primary_key=True, nullable=False)
    device = Column(String(50), nullable=False, comment='设备')
    data = Column(Text(500), nullable=False, comment='数据')
    data_report_at = Column(DateTime, nullable=False, comment='数据上报时间')
    created_at = Column(DateTime, nullable=False, comment='数据入库时间')
