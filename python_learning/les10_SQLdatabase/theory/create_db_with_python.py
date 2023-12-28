import sqlite3 as sql

with sql.connect('created_db_with_python.db') as db:
    # db.cursor().execute('''
    #     INSERT INTO PRICES (name, price, color)
    #     VALUES ('product seven', 80, 'blue'),
    #         ('product eight', 90, 'green'),
    #         ('product nine', 100, 'orange');
    # ''')
    # db.commit()
    # Создаём курсор
    cursor = db.cursor()
    cursor.execute(
        '''SELECT * FROM PRICES;'''
    )
    print(cursor.fetchall())
