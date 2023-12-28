import sqlite3


def get_result(name: str) -> None:
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute(
        """DELETE FROM films
                WHERE title LIKE ? AND title LIKE ?""",
        ('Я%', '%а')
    )
    conn.commit()
    conn.close()
