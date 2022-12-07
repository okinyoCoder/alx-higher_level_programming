#!/usr/bin/python3
'''Script that lists all states from database hbtn_0e_0_usa '''

import MySQLdb
from sys import argv

def state_List(username, password, databaseName):
    ''' print all states in the database '''

    dbase = MySQLdb.connect(
            host = "localhost",
            port = 3306,
            user = "username",
            passwd = "password",
            db = "databaseName"
            )

    cur = dbase.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    dbase.close()

if __name__ == "__main__":
    argv = sys.argv[1:]
    username, password, databaseName = argv
    state_List(username, password, databaseName)
