import sqlite3 as sql
# import PyQ

def print_films(db_name: str) -> str:
    with sql.connect(db_name) as db:
        cur = db.cursor()
        res = cur.execute(
            """SELECT title FROM films WHERE genre IN
                ((SELECT id FROM genres WHERE title = ?),
                (SELECT id FROM genres WHERE title = ?))
                AND year >= ?""",
            ('музыка', 'анимация', '1997')
        ).fetchall()
        return '\n'.join([tpl[0] for tpl in res])

db_name = input()
# db_name = r'SQLdatabase\theory\films_db.sqlite'
print(print_films(db_name))
