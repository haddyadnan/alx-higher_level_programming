#!/usr/bin/python3


"""
Write a script that lists all states from the database hbtn_0e_0_usa
where name matches the argument."""

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
    c.execute(
        """SELECT *
                FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY id ASC""".format(
            argv[4]
        )
    )
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
