from sqlalchemy import Column, Integer, String, Text, DateTime
from . import Base


class NodeData(Base):
    """
    【节点数据表】实体类
    """

    __tablename__ = 'node_data'

    id = Column(Integer, primary_key=True, nullable=False)
    node = Column(String(300), nullable=False, comment='节点')
    data = Column(Text(500), nullable=False, comment='数据')
    created_at = Column(DateTime, nullable=False, comment='时间')
