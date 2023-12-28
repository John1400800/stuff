import sqlite3
import csv

db_name = input()
years = tuple(map(int, input().split()))
sql_query = """SELECT ships.ship, captains.captain,
navigators.navigator, year, benefit
FROM ships
INNER JOIN captains ON ships.id_cap = captains.id_cap
INNER JOIN navigators ON ships.id_navigator = navigators.id_navigator
WHERE (captains.captain = 'Billy Bons'
OR navigators.navigator = 'Billy Bons')
AND year BETWEEN ? AND ?
ORDER BY ships.id"""

db_conn = sqlite3.connect(db_name)
cur = db_conn.cursor()

res = cur.execute(sql_query, years).fetchall()

with open('pirates.csv', 'w', newline='') as csv_f:
    writer = csv.writer(csv_f, delimiter=';', quotechar='"')
    writer.writerows(res)
