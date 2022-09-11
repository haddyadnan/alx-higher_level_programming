#!/usr/bin/python3


"""
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
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
        """SELECT cities.name
                FROM cities,states
                WHERE cities.state_id=states.id and states.name LIKE '{}'
                ORDER BY cities.id ASC""".format(
            param
        )
    )
    rows = c.fetchall()
    print(", ".join([row[0] for row in rows]))
    print()
    c.close()
    db.close()
