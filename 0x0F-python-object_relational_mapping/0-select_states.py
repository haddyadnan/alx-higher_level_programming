#!/usr/bin/python3


import MySQLdb
from sys import argv

"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""


def main():
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )
    # c = db.cursor()
    # c.execute("SELECT * FROM states ORDER BY id ASC")
    # rows = c.fetchall()
    # for row in rows:
    #     print(row)
    # c.close()
    # db.close()

    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states ORDER BY id ASC"
    )  # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":

    main()
