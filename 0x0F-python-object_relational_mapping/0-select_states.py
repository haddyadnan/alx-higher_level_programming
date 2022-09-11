#!/usr/bin/python3
import MySQLdb
from sys import argv

"""
Write a script that lists all states from the database hbtn_0e_0_usa:
"""

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], db=argv[2], passwd=argv[3], port=3306
    )
    c = db.cursor()
    c.execute(
        """SELECT *
              FROM states
              ORDER BY id ASC"""
    )
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
