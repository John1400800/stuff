import sqlite3 as sql


def end_with_a_question(name_db: str) -> str:
    with sql.connect(name_db) as db:
        c = db.cursor()
        res = c.execute(
            '''SELECT title FROM films
                    WHERE title LIKE '%?';'''
        ).fetchall()
    res = '\n'.join([el[0] for el in res])
    return res


db_name = input()
# db_name = r'SQLdatabase\theory\films_db.sqlite'
print(end_with_a_question(db_name))
