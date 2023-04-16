#!/usr/bin/python3
""" script that takes in an argument and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument
"""
import MySQLdb
from sys import argv

dbase = MySQLdb.connect(
        user="argv[1]"
        passwd="argv[2]"
        db="argv[3]")

cur = dbase.Cursor()
cur.execute("SELECT * FROM states WHERE name='{argv[4]}' \
         ORDER BY states.id ASC")
rows = cur.fetchall()

for row in rows:
    print(row)
cur.close()
dbase.close()
