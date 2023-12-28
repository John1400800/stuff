import sqlite3

db_name = input()
field = input()
first_condition = input()
operator = input()
secont_condition = input()

sql_query = (f"SELECT {field} FROM Stories WHERE "
             + f"{first_condition} {operator} {secont_condition}"
             + f" ORDER BY {field}")

db_conn = sqlite3.connect(db_name)
cur = db_conn.cursor()
print(*[tpl[0] for tpl in cur.execute(sql_query).fetchall()], sep='\n')
