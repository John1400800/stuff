import sqlite3 as sql


def take_year(db_name):
    with sql.connect(db_name) as db:
        c = db.cursor()
        res = c.execute(
            '''SELECT DISTINCT year FROM films
                    WHERE title LIKE 'Х%';'''
        ).fetchall()
    return '\n'.join([str(el[0]) for el in res])


db_name = r'SQLdatabase\theory\films_db.sqlite'
# db_name = input()
print(take_year(db_name))
