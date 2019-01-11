import pyodbc 
import pandas as pd
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=[SERVERNAME];Database=[DATABASE];UID=[DB_USER];PWD=[USER_PW]")
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM P_ORDER')

for row in cursor:
    print (row)
    
input()