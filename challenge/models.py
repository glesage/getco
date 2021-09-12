from sqlalchemy import Column, Integer, String
from .database import Base


class Challenge(Base):
    __tablename__ = 'challenges'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
