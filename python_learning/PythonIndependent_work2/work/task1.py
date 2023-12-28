import sys
import sqlite3

db_name, secont_condition, operator = sys.stdin.read().splitlines()

sql_query = ("SELECT name FROM ship_team WHERE status = 'sailor'"
             + f' {operator} '
             + secont_condition
             + 'ORDER BY age')

db_conn = sqlite3.connect(db_name)
cur = db_conn.cursor()
print(*[tpl[0] for tpl in cur.execute(sql_query).fetchall()], sep='\n')
