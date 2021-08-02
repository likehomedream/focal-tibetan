from sqlalchemy import Column, Integer, String
from msg.database import Base


class MSG(Base):
    __tablename__ = 'msg'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    msg_id = Column(String)
    msg_str_bo_CN = Column(String)
    msg_str_zh_CN = Column(String)
