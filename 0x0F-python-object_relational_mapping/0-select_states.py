#!/usr/bin/python3


import MySQLdb
from sys import argv

"""
Write a script that lists all states from the database hbtn_0e_0_usa:
"""

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
