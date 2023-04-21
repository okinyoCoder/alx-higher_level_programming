#!/usr/bin/python3
""" file contains the class definition of a City"""
from sqlalchemy import column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """class represent table City of a database"""
    __tablename__ = "cities"
    id = Column(Integer, Primary_Key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey=('states.id'))
