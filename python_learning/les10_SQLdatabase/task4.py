import sqlite3 as sql


def comedy_an_hour_or_more(name_db):
    with sql.connect(name_db) as db:
        c = db.cursor()
        c.execute(
            """SELECT title FROM films
                WHERE genre = (SELECT id FROM genres WHERE title = 'комедия')
                    AND duration >= 60;"""
        )

        return '\n'.join([el[0] for el in c.fetchall()])


# name_db = r'les10_SQLdatabase\theory\films_db.sqlite'
name_db = input()
print(comedy_an_hour_or_more(name_db))
