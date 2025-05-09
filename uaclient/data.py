from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Data(Base):
    """
    【警报数据表】实体类
    """

    __tablename__ = 'data'

    id = Column(Integer, primary_key=True, nullable=False)
    node = Column(String(300), nullable=False, comment='节点')
    data = Column(String(500), nullable=False, comment='数据')
    created_at = Column(DateTime, nullable=False, comment='时间')
