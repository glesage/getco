from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from .database import Base


class Challenge(Base):
    __tablename__ = 'challenges'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    author_user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', back_populates='challenges_authored')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    password = Column(String)
    challenges_authored = relationship('Challenge', back_populates='author')
