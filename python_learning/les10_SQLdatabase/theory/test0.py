import sqlite3 as sql

with sql.connect(r'SQLdatabase\theory\films_db.sqlite') as film_db:
    cursor = film_db.cursor()
    res = cursor.execute(
        """SELECT id, title, year, duration FROM films
	WHERE genre = (SELECT id FROM genres
		                WHERE title = ?)
                    AND title LIKE ?
                    AND duration > ?
                    AND year > ? AND year < ?""",
        ('драма', 'Кре%ц%', 70, 1970, 2005)
    ).fetchall()

    res2 = cursor.execute(
        'SELECT * FROM films WHERE title LIKE "Из%" AND year > 2001').fetchmany(100)

for el in res:
    print(el)

print('\n\n')

for el in res2:
    print(el)
