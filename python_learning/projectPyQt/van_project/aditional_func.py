from const_and_query import *
import sqlite3
from string import ascii_lowercase, digits
from random import sample, choice, randint


class IncorrectParameters(Exception):
    pass


class MinimumMoreMaximum(IncorrectParameters):
    pass


class IncorectMinimum(IncorrectParameters):
    pass


class ImpossibleNumCities(IncorrectParameters):
    pass


def make_data_dct(
    data_f_name: str = DATA_PATH,
) -> dict[str, list[str]]:
    '''запись даных из файла в словарь'''
    f_open = open(data_f_name)
    f_data = f_open.read()
    f_open.close()

    data_dct = {}
    for s in f_data.split('\n\n'):
        key, val = s.split(':\n')
        data_dct[key] = val.replace('\n', ' ').split(', ')

    return data_dct


def sql_insert_queries(
    data_dct: dict[str, list[str]],
    num_of_cities: int,
    average_price: int,
    # минимально / максимально отелей в городе
    num_hotels_in_city: tuple[int, int] = (1, 1),  # (4, 8)
    # минимально / саксимально количество мест в отелях
    num_seats_in_hotels: tuple[int, int] = (1, 1)  # (4, 7)
) -> tuple[str, str, str]:
    '''формирование sql запросов'''

    for tpl in (num_hotels_in_city, num_seats_in_hotels):
        if tpl[0] > tpl[1]:
            raise MinimumMoreMaximum(
                'минимум больше максимума')

    if num_seats_in_hotels[0] < 1:
        raise IncorectMinimum(
            'в отелях должно быть как минимум одно место')

    # вызов ошибки если количество городов больше или меньше
    # чем возможно сгенерировать
    if (
        num_of_cities < 1 or
        num_of_cities > len(data_dct['cities'])
    ):
        raise ImpossibleNumCities(
            'нельзя сгенерировать столько городов')

    # генерация названий городов по числу num_of_cities
    cities = sample(data_dct['cities'], num_of_cities)

    # генерация номеров виз по числу
    # num_of_cities из symbs
    symbs = ascii_lowercase + digits
    visa_codes = tuple([''.join([choice(symbs) for s in range(5)])
                       for _ in range(len(cities))])

    lst_cities_data: list[tuple[str, int]] = []
    lst_hotels_data: list[tuple[str, int, int, int]] = []
    lst_people_data: list[tuple[str, str, int]] = []

    id_hotel = 0
    for ic, city in enumerate(cities):
        num_hotels = randint(*num_hotels_in_city)
        lst_cities_data.append((city, visa_codes[ic]))
        id_city = ic + 1

        for _ in range(num_hotels):
            name_hotel = (
                choice(data_dct['first_word']) + ' '
                + choice(data_dct['second_word']))
            max_people = randint(*num_seats_in_hotels)
            num_guest = randint(0, max_people)
            price = randint(int(average_price * 0.7), int(average_price * 1.2))
            lst_hotels_data.append(
                (name_hotel, id_city, max_people, num_guest, price))
            id_hotel += 1

            for _ in range(num_guest):
                name_people = (
                    choice(data_dct['people_names']) + ' '
                    + choice(data_dct['people_surnames']))
                lst_people_data.append((name_people,
                                        visa_codes[ic],
                                        id_hotel))

    sql_query1 = (
        SQL_HALF_INSERT_CITIES
        + ',\n'.join([f'''("{tpl[0]}", "{tpl[1]}")'''
                      for tpl in lst_cities_data]))

    sql_query2 = (
        SQL_HALF_INSERT_HOTELS
        + ',\n'.join(
            [f'''("{tpl[0]}", {tpl[1]}, {tpl[2]}, {tpl[3]}, {tpl[4]})'''
             for tpl in lst_hotels_data])) if lst_hotels_data else ''

    sql_query3 = (
        SQL_HALF_INSERT_PEOPLE
        + ',\n'.join(
            [f'''("{tpl[0]}", "{tpl[1]}", {tpl[2]})'''
             for tpl in lst_people_data])) if lst_people_data else ''

    return sql_query1, sql_query2, sql_query3


# тесты
if __name__ == '__main__':
    db_conn = sqlite3.connect(DB_PATH)
    cur = db_conn.cursor()
    cur.executescript(SQL_CREATE_DB)
    db_conn.commit()
    # cur.executescript(SQL_DELETE_DB)
    # db_conn.commit()

    for sql_query in sql_insert_queries(
        make_data_dct(),
        4, 1000,
        (0, 7), (1, 3)
    ):
        if sql_query:
            cur.execute(sql_query)
            db_conn.commit()
