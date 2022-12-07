#!/usr/bin/python3
"""
script that list all states with name starting with N
from a database hbtn_0e_0_usa 
"""
import MySQLdb
from sys import argv

if __name __ == '__main__':
    dbase = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = dbase.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name \ 
            LIKe 'N%' ORDER BY state.id ASC"
            )
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    dbase.close()
