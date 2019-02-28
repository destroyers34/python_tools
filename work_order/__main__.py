import pyodbc
import os
from openpyxl import *
from connection.connect_string import *
from email_manager.quickstart import *
from work_order.fix_borders import patch_worksheet


def main():
    po_number = input('Inscrire numéro de PO:')
    current_folder = os.path.dirname(os.path.abspath(__file__))
    save_path = "%s\\Work order T%s.xlsx" % (current_folder, po_number)
    cursor = connect_to_erp()
    wb = get_parts_po(cursor, po_number)
    wb.save(save_path)


def get_parts_po(cursor, po_number):
    sqlquery = (
        "SELECT C.PO, MIN(C.SUPP_PROD_NO), MIN(C.QTY) QTY, ISNULL(B.JOB_NO, 'N/A'), "
        "ISNULL(MIN(LEFT(D.DOC_NAME,7)),'N/A') PROJECT_NO "
        'FROM P_ORDER_DTL C '
        'LEFT JOIN P_ORDER_SUBDTL A on A.ITEM_NO = C.ITEM_NO and A.PO = C.PO '
        "LEFT JOIN ITEM_SCHEDULING B on CONCAT(B.PROJECT_NO,'-',B.ITEM_NO) = A.JOB_NO "
        'LEFT JOIN PROJET D on D.PROJECT_NO = B.PROJECT_NO '
        'WHERE C.po={} and C.SELECTED_ITEM=1 '
        'GROUP by C.po, C.ITEM_NO, B.JOB_NO '
        'ORDER by C.item_NO'.format(po_number))
    # print(sqlquery)
    cursor.execute(sqlquery)
    patch_worksheet()
    wb = load_workbook('template.xlsx')
    ws = wb.active
    for row in cursor:
        ws1 = wb.copy_worksheet(ws)
        ws1.set_printer_settings(1, 'landscape')
        # ws1.sheet_properties.pageSetUpPr.fitToPage = True
        part = row[1]
        part = part.split('_')
        ws1.title = part[0]
        # NUMERO PIECE
        ws1['A9'] = part[0]
        # REVISION
        ws1['AB9'] = part[1]
        # QUANTITÉ
        ws1['AH9'] = row[2]
        # NUMERO MACHINE
        ws1['AP9'] = row[4]
        # JOB_NO
        ws1['BD9'] = row[3]
        # PO
        ws1['BR9'] = row[0]
        # print('\n')
    # print(wb.sheetnames)
    wb.remove(wb['sheet1'])
    return wb


def connect_to_erp():
    cnxn = pyodbc.connect(connect_string())
    return cnxn.cursor()


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
