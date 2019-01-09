import pyodbc 
import pandas as pd
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=SKYWARP\PMESYMBIOSE;Database=ETI;UID=sa;PWD=Elfido1234")
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM P_ORDER')

for row in cursor:
    print (row)
    
input()