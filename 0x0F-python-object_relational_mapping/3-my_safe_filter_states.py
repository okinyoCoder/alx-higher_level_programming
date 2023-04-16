#!/usr/bin/python3
""" script that takes in an argument and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    dbase = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cur = dbase.cursor()
    cur.execute("SELECT * FROM states WHERE name= %s \
        ORDER BY states.id ASC", (argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    dbase.close()
