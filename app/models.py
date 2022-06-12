from sqlalchemy import TIMESTAMP, Column, Integer,Boolean,String
from sqlalchemy.sql.expression import text
from .database import Base

class Call(Base):
    __tablename__= "calls"
    user_name = Column(String, primary_key = True, nullable =False)
    call_duration = Column(Integer, nullable = False)
    call_count = Column(Integer, nullable = False)
    block_count = Column(Integer, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default=text('now()') )