#!/usr/bin/python3
""" script that prints the first State object from
    the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    dbase_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(dbase_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    for obj in session.query(State).whereclause(State.id == 1):
        if session.query(State) is not None:
            print("{}: {}".format(obj.id, obj.name))
        else:
            print("nothing")
