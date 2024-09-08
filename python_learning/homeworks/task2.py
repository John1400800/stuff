import sqlite3
from tabulate import tabulate

DB_PATH                 = 'films.db'
SQL_GET_TABLE_NAMES     = "SELECT name FROM sqlite_master WHERE type='table';"
SQL_GET_TABLE_INFO      = "PRAGMA table_info({});"
SQL_GET_TABLE_DATA      = "SELECT * FROM {};"

SQL_CREATE_DB           = """
CREATE TABLE IF NOT EXISTS FILMS (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT,
    director    TEXT,
    year        INTEGER,
    genre       TEXT
);
"""

SQL_INSERT_INTO_TABLES  = """
INSERT INTO FILMS(title, director, year, genre)
VALUES
    ('Inception', 'Christopher Nolan', 2010, 'Sci-Fi'),
    ('The Matrix', 'Lana Wachowski, Lilly Wachowski', 1999, 'Sci-Fi'),
    ('Parasite', 'Bong Joon-ho', 2019, 'Thriller'),
    ('The Godfather', 'Francis Ford Coppola', 1972, 'Crime'),
    ('Pulp Fiction', 'Quentin Tarantino', 1994, 'Crime');
"""

def create_tables(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(SQL_CREATE_DB)
        conn.commit()

def insert_into_tables(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        if cursor.execute("SELECT COUNT(*) FROM FILMS").fetchall()[0][0] == 0:
            cursor.execute(SQL_INSERT_INTO_TABLES)
            conn.commit()

def fetch_data(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        for name in (table[0] for table in cursor.execute(SQL_GET_TABLE_NAMES).fetchall()):
            print(f"\nTable {name}:")
            print("\t".join(info[1] for info in cursor.execute(
                SQL_GET_TABLE_INFO.format(name)).fetchall()))
            print("\n".join("\t".join(str(data) for data in row)
                            for row in cursor.execute(
                                SQL_GET_TABLE_DATA.format(name)).fetchall()))

def get_film_by_year(db_path, year):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        print(
        ", ".join(title[0] for title in cursor.execute("SELECT title FROM FILMS WHERE year >= ?", (year,)).fetchall()))


if __name__ == "__main__":
    create_tables(DB_PATH)
    insert_into_tables(DB_PATH)
    # fetch_data(DB_PATH)
    get_film_by_year(DB_PATH, input("Введите год выпуска кинофильма: "))

