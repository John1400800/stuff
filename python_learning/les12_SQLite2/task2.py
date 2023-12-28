import sqlite3


def get_result(name: str) -> None:
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute(
        """UPDATE films
            SET duration = 42
            WHERE duration = ?""",
        ('',)
    )
    conn.commit()
    conn.close()
