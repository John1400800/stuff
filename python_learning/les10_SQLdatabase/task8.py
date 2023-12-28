import sqlite3


def main_func(db_name: str) -> str:
    with sqlite3.connect(db_name) as films_db:
        c = films_db.cursor()
        c.execute(
            """SELECT title FROM films
                    WHERE title LIKE '%Астерикс%'
                    AND title NOT LIKE '%Обеликс%';"""
        )
        return '\n'.join([tpl[0] for tpl in c.fetchall()])


# db_name = r'les10_SQLdatabase\theory\films_db.sqlite'
db_name = input()
print(main_func(db_name))
