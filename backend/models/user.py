from database import Base
from sqlalchemy import DateTime,Boolean,Column,String,Integer
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True,index=True)
    
    First_Name = Column(String(100),nullable=False)
    Last_Name = Column(String(100),nullable=False)
    
    email = Column(String(150),unique=True,nullable=False,index=True)
    password = Column(String(100),nullable=False)
    
    role = Column(String(50),nullable=False,default="employee")
    
    is_active = Column(Boolean,default=True)
    
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    
    updated_at = Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())
    
    