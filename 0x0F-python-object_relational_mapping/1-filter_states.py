#!/usr/bin/python3
"""
script that list all states with name starting with N
from a database hbtn_0e_0_usa 
"""
import MySQLdb
from sys import argv

def search_state(username, password, databaseName):
    dbase = MySQLdb.connect(
            host="localhost",
            port=3306,
            user="username",
            passwd="password",
            db="databaseName"
            )
    cur = dbase.cursor()
    cur.execute(
            """SELECT * FROM states WHERE name 
            LIKe 'N%' ORDER BY state.id ASC"""
            )
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    dbase.close()

if __name__ == "__main__":
    username=argv[1], 
    password=argv[2], 
    databaseName=argv[3]
    search_state(username, password, databaseName)
