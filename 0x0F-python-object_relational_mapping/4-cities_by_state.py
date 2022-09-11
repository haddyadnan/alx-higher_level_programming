#!/usr/bin/python3


"""
Write a script that lists all cities from the database hbtn_0e_4_usa
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

    c.execute(
        """SELECT cities.name, states.name
                FROM cities,states
                WHERE cities.state_id=states.id
                ORDER BY cities.id ASC"""
    )
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
