'''#'''
import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'InsuranceDashboardData',
    user = 'postgres',
    password = 'admin@1234',
    port = 5432
)

# print(conn)

SqlQuery = 'select * from "InsuranceDashboard_kaggletestinsurance" limit 100'

cursor_1 = conn.cursor()

results = cursor_1.execute(SqlQuery)

rows = cursor_1.fetchall()

for each_row in rows:
    print(each_row)
