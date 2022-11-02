# '''#'''
# import datetime as dt
# import psycopg2
# import pandas as pd
 
# hostStr = 'localhost'
# dbPort = 5432
# dbStr = 'InsuranceDashboardData'
# uNameStr = 'postgres'
# dbPassStr = 'admin'

# try:
#     conn = psycopg2.connect(host=hostStr, port=dbPort, dbname=dbStr, user=uNameStr, password=dbPassStr)

#     # get a cursor object from the connection
#     cur = conn.cursor()

#     # use the cursor object to run SQL commands to perform operations like fetch rows, insert rows, update rows, delete rows etc.



#     sqlStr = "select name, dob, studentid from public.students \
#         where dob >= %s and studentid > %s \
#         order by name, studentid"

#     # execute the data fetch SQL command along with the SQL placeholder values
#     cur.execute(sqlStr, (dt.datetime(2018, 1, 1, 0, 0, 0), 3000))

#     rowCount = cur.rowcount
#     print("number of fetched rows =", rowCount)

#     # fetch all the records from cursor
#     records = cur.fetchall()
#     # get the column names of the fetched records
#     colNames = [row[0] for row in cur.description]

#     # iterate through all the fetched records
#     for rowIter in range(len(records)):
#         print("reading data from {0} row".format(rowIter))
#         rowTuple = records[rowIter]
#         print("name =", rowTuple[0])
#         print("dob =", rowTuple[1])
#         print("studentId =", rowTuple[2])

#     # create a dataframe from the fetched records (optional)
#     recordsDf = pd.DataFrame.from_records(records, columns=colNames)




#     # if(conn):
#     #     # close the cursor object to avoid memory leaks
#     #     cur.close()
#     #     # close the connection object also
#     #     conn.close()
        
# except (Exception, psycopg2.Error) as error:
#     print("Error while interacting with PostgreSQL...\n", error)
#     records = 0  
