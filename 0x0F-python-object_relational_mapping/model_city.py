#!/usr/bin/python3
""" file contains the class definition of a City"""
from sqlalchemy import column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """class represent table City of a database"""
    __tablename__ = "cities"
    id = Column(Integer, PrimaryKey=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey='states.id')
