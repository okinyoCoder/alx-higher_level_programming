#!/usr/bin/python3
"""file contains the class definition of a City"""
from sqlalchemy import column, String, Integer, ForeignKey
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base


class city(Base):
    """class represent table City of a database"""

    __tablename__ = "cities"
    id = Column(Integer, Primary_Key=True)
    state_id = Column(Integer, nullable=False, ForeignKey=('states.id'))
    name = Column(String(128), nullable=False)
