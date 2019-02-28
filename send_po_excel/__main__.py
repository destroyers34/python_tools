import pyodbc
import pandas as pd
import os
from connection.connect_string import *
from email_manager.quickstart import *


def main():
    po_number = input('Inscrire numéro de PO:')
    current_folder = os.path.dirname(os.path.abspath(__file__))
    save_path = "%s\\T%s.xlsx" % (current_folder, po_number)
    cursor = connect_to_erp()
    df = get_parts_po(cursor, po_number)
    print(df)
    save_to_excel(df, save_path)
    email_po(po_number, "%s\\T%s.xlsx" % (current_folder, po_number))


def get_parts_po(cursor, po_number):
    cursor.execute('SELECT * FROM P_ORDER_DTL WHERE PO={}'.format(po_number))
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
    return pd.DataFrame({column_title[0]: parts_no, column_title[1]: descriptions, column_title[2]: qantites})


def save_to_excel(df, save_path):
    writer = pd.ExcelWriter(save_path)
    df.to_excel(writer, sheet_name='sheet11', index=False)
    writer.save()


def connect_to_erp():
    cnxn = pyodbc.connect(connect_string())
    return cnxn.cursor()


def email_po(po_number, file):
    service = create_service()
    # results = service.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])

    # if not labels:
    #    print('No labels found.')
    # else:
    #    print('Labels:')
    #    for label in labels:
    #        print(label['name'])
    message = create_message_with_attachment('abechard@centreidnov.com',
                                             'abechard@centreidnov.com',
                                             "Commande PO#%s" % po_number,
                                             "Bonjour\nVoici des pièces à produire",
                                             file)
    #send_message(service, 'me', message)


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
