#!/usr/bin/python3
""" file contains the class definition of a City"""
from sqlalchemy import column, String, Integer, ForeignKey
from model_state import Base, State


class City(Base):
    """class represent table City of a database
    Args:
        Base():
    Attribute:
         __tablename__(str): name of the class 
         id(int): primary_key of cities table
         name(str): names of cities
         state_id(int): foreign_key that link to state id
    """
    __tablename__ = 'cities'
    id = Column(Integer, PrimaryKey=True,nullable=False )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey='states.id')
