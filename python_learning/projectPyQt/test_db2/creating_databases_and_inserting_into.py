from random import sample
from string import ascii_lowercase, digits
import sqlite3


def rand_pass(
    sym: str,
    num_of_opt: int,
    num_of_passwrds: int
) -> list[str]:
    '''Генерация рандомных паролей,
    для паролей из малого количества символов
    эта функция не подайдёт :-('''
    # следуящая строка огранечения генерации
    if num_of_passwrds <= (len(sym)**num_of_opt) * (17 / 100):
        res = []
        cnt = 0
        while cnt != num_of_passwrds:
            password = ''.join(sample(sym, num_of_opt))
            if password not in res:
                cnt += 1
                res.append(password)
        return res
    raise Exception(
        f'сложно составить {num_of_passwrds} паролей из {num_of_opt}' +
        f'значного пороля где каждая ячейка может принять {len(sym)} значений')


symbs = ascii_lowercase + digits

num_of_countries = 5
CODES = rand_pass(symbs, 5, num_of_countries)

# путь к файлу базы данных
NAME_DB = r'projectPyQt\test_db\hoteles.db'

ALL_COUNTRIES: dict = {
    'Germany':
    (
        '+49', CODES[0],
        ('Berlin', 'Hamburg', 'Munich', 'Cologne')
    ),
    'Great Britain':
    (
        '+44', CODES[1],
        ('London', 'Edinburgh', 'Royal Windsor', 'Roman-Era Bath')
    ),
    'France':
    (
        '+33', CODES[2],
        ('Paris', 'Marseille', 'Nice', 'Normandy')
    ),
    'Netherlands':
    (
        '+31', CODES[3],
        ('Amsterdam', 'Utrecht', 'Maastricht', 'Delft')
    ),
    'Poland':
    (
        '+48', CODES[4],
        ('Krakow', 'Warsaw', 'Gdansk', 'Wroclaw')
    )
}


def insert_countries_sql_query(
    half_sql_query: str,
) -> str:
    '''генерация sql запроса
    для создания таблицы COUNTRIES'''
    sql_query = (
        half_sql_query
        + ',\n'.join([
            f"('{key}', '{val[0]}', '{val[1]}')"
            for key, val in ALL_COUNTRIES.items()
        ]))

    return sql_query


def insert_cities_sql_query(
        half_sql_query: str,
        dct_name_id_countries: dict
) -> str:
    '''генерация sql запроса
    для создания таблицы CITIES'''

    # создание списка кортэжей типа:
    # город, идентификатор страны в которой этот город
    sql_query_extension = []
    for k, v in ALL_COUNTRIES.items():
        for city in v[2]:
            sql_query_extension.append(
                (city, dct_name_id_countries[k]))

    # получение из сгенерированного выше списка sql запроса
    sql_query = (
        half_sql_query
        + ',\n'.join([
            f"('{tpl[0]}', {tpl[1]})"
            for tpl in sql_query_extension
        ]))

    return sql_query


if __name__ == '__main__':

    sql_query_create_db = '''
CREATE TABLE IF NOT EXISTS HOTELS (
    id_hotel INTEGER,
    id_city INTEGER,
    name_of_hotel TEXT,
    discription TEXT,
    PRIMARY KEY (id_hotel AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS ROOMS (
    id_room INTEGER,
    num_of_bed INTEGER,
    id_hotel INTEGER,
    id_people INTEGER,
    PRIMARY KEY (id_room AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS PEOPLES (
    id_people INTEGER,
    name TEXT,
    phone_num INTEGER,
    passport_cod INTEGER,
    id_city INTEGER,
    PRIMARY KEY (id_people AUTOINCREMENT)

);

CREATE TABLE IF NOT EXISTS CITIES (
    id_city INTEGER,
    name_city TEXT,
    id_country INTEGER,
    PRIMARY KEY (id_city AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS COUNTRIES (
    id_country INTEGER,
    name_of_country TEXT,
    phone_cod TEXT,
    passport_cod TEXT,
    PRIMARY KEY (id_country AUTOINCREMENT)
);'''

    f1_n_with_sql_query = r'projectPyQt\test_db\insert_into_countries.sql'
    f2_n_with_sql_query = r'projectPyQt\test_db\insert_into_cities.sql'

    sql_query_get_id_countries = (
        'SELECT name_of_country, id_country FROM COUNTRIES')

    with sqlite3.connect(NAME_DB) as db_conn:
        cur = db_conn.cursor()

        cur.executescript(
            sql_query_create_db)

        f1 = open(f1_n_with_sql_query)
        half_sql_query1 = f1.read() + ' '
        f1.close()

        f2 = open(f2_n_with_sql_query)
        half_sql_query2 = f2.read() + ' '
        f2.close()

        cur.executescript(
            insert_countries_sql_query(half_sql_query1))
        db_conn.commit()

        lst_name_id_countries = cur.execute(
            sql_query_get_id_countries).fetchall()

        COUNTRIES_AND_THEIR_IDS: dict = {
            countrie: i
            for countrie, i in lst_name_id_countries}

        cur.execute(
            insert_cities_sql_query(half_sql_query2,
                                    COUNTRIES_AND_THEIR_IDS))
        db_conn.commit()
