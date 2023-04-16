#!/usr/bin/python3
""" script that lists all cities from
    the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbase = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cur = dbase.cursor()
    cur.execute("SELECT * FROM cities ORDER BY cities.id ASC")
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    dbase.close()
