#!/usr/bin/python3
"""script that changes the name of a State
   object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(engine)
    session = Session()
    obj = session.query(State).filter(State.id == 2).first()
    obj.name = "New Mexico"
    session.commit()

    session.close()
