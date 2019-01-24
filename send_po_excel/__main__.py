import pyodbc
import pandas as pd
import os
from connection.connect_string import *
from email_manager.quickstart import *

po_number = input('Inscrire numéro de PO:')
currentfolder = os.path.dirname(os.path.abspath(__file__))
writer = pd.ExcelWriter("%s\\T%s.xlsx" % (currentfolder, po_number))


def main():
    cursor = connect_to_erp()
    cursor.execute(('SELECT * FROM P_ORDER_DTL WHERE PO={}').format(po_number))
    column_title = ['NUMERO', 'DESCRIPTION', 'QTY']
    parts_no = []
    descriptions = []
    qantites = []
    for row in cursor:
        # print("%s, %s, %s" % (row[3], row[5], int(row[6])))
        parts_no.append(row[3])
        descriptions.append(row[5])
        qantites.append(row[6])
        # print('\n')
    df = pd.DataFrame({column_title[0]: parts_no, column_title[1]: descriptions, column_title[2]: qantites})
    print(df)
    df.to_excel(writer, sheet_name='sheet11', index=False)
    writer.save()
    email_po()


def connect_to_erp():
    cnxn = pyodbc.connect(connect_string())
    return cnxn.cursor()


def email_po():
    service = create_service()
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
