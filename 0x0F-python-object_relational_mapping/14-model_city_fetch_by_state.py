#!/usr/bin/python3
"""script that prints all City objects from
   the database hbtn_0e_14_usa
"""
from model_state import Base, State, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(engine)
    session = Session()

    result = session.query(City, State).join(State)
    for city, state in result.all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.commit()
    session.Close()
