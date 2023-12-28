import csv
import sqlite3

db_name = input()
place_title, loophole_number = input().split()

sql_query = """SELECT Team.name, Team.weapon, Schedule.time_on_duty 
FROM Schedule INNER JOIN Team ON Schedule.team_id = Team.id
INNER JOIN Places_to_protect ON Schedule.place_id = Places_to_protect.id
WHERE Places_to_protect.title = ?
AND Schedule.loophole_number = ?
ORDER BY time_on_duty"""

db_conn = sqlite3.connect(db_name)
cur = db_conn.cursor()
res = cur.execute(sql_query, (place_title, loophole_number)).fetchall()

with open('on_duty.csv', 'w', newline='') as csv_f:
    writer = csv.writer(csv_f, delimiter=';', quotechar='"')
    for tpl in res:
        writer.writerow(list(tpl))
