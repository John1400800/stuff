import sys
import sqlite3

# ввод
db_name, operator, *conditions = sys.stdin.read().splitlines()

# sql запрос
sql_query = ('SELECT phrase FROM stories\nWHERE '
             + f' {operator} '.join(conditions)
             + "\nORDER BY priority DESC")

db_conn = sqlite3.connect(db_name)
cur = db_conn.cursor()
res = [
    tpl[0]
    for tpl in cur.execute(sql_query).fetchall()]

print(*res, sep='\n')
