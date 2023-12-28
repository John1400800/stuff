import sqlite3


def get_result(name_db: str) -> None:
    conn = sqlite3.connect(name_db)
    cursor = conn.cursor()
    cursor.execute(
        """DELETE FROM films
                WHERE genre = 
                (SELECT id FROM genres
                    WHERE title = ?)
                AND duration >= 90""",
        ('боевик')
    )
    conn.commit()
    conn.close()
