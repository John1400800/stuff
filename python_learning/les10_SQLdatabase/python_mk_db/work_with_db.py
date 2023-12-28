import sqlite3

with sqlite3.connect(r'SQLdatabase\python_mk_db\test.db') as db_conn:
    #! Создадим курсор который позволит выполнять некотрые SQL команды
    c = db_conn.cursor()
    #! Синтаксис для ввода команд
    # c.execute(
    #     """CREATE TABLE employees (
    #         name VARCHAR(5),
    #         surname VARCHAR(5),
    #         pay INTEGER
    #         );"""
    # )

    #! commit Фиксирует изменение
    db_conn.commit()
    #! Добавляем информацию в иаблицу employees
    # c.execute(
    #     """INSERT INTO employees VALUES ('Harry', 'Thomas', 500),
    #         ('Lois', 'Norton', 600),
    #         ('Catherine', 'Chandler', 700)"""
    # )
    #! Выбераем все столбики из таблицы employees
    c.execute(
        "SELECT * FROM employees"
    )

    print(c.fetchall())
