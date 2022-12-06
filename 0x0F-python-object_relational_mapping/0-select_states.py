#!/usr/bin/python3
'''Script that lists all states from database hbtn_0e_0_usa '''

import MySQLdb
import sys

def state_List(username, password, databaseName):
    ''' print all states in the database '''
    dbase = MySQLdb.connect(
            host = "localhost",
            port = 3306,
            user = "username"
            passwd = "password"
            db = "databaseName"
            )
    cur = dbase.cursor()
    cur.execute("SELECT * FROM  state ORDER BY state.id ASC")
    result = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    dbase.close()

if __name__ == "__main__":
    argv = sys.argv[1:]
    username, password, databaseName = argv
    state_List(username, password, databaseName)
