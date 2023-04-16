#!/usr/bin/python3
""" script that lists all states
with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbase = MYSQLdb.connect(
            host="localhost",
            port="3306",
            user="argv[1]",
            passwd="argv[2]",
            db="argv[3]")
    cur = dbase.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    dbase.close()
