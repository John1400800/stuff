import sqlite3


def get_result(name: str) -> None:
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute(
        """
    DELETE FROM films
        WHERE genre = (
            SELECT id FROM genres
                WHERE title = ?)
        """,
        ('комедия',)
    )
    conn.commit()
    conn.close()


db_name = r'les12_SQLite2\films_db.sqlite'
get_result(db_name)
