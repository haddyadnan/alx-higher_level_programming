#!/usr/bin/python3


"""
Write a script that lists all states from the database hbtn_0e_0_usa
where name matches the argument - prevent sql injection
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )
    c = db.cursor()
    param = argv[4].split(";")[0]
    c.execute(
        """SELECT *
                FROM states
                WHERE name LIKE '{}'
                ORDER BY id ASC""".format(
            param
        )
    )
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
