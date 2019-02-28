import pyodbc
import pandas as pd
import os
from connection.connect_string import *


def main():
    po_number = input('Inscrire numéro de PO:')
    current_folder = os.path.dirname(os.path.abspath(__file__))
    save_path = "%s\\T%s.xlsx" % (current_folder, po_number)
    cnxx = pyodbc.connect(connect_string())
    df = get_project_no(cnxx, po_number)
    #print(df)
    save_to_excel(df, save_path)
    cnxx.close()


def get_project_no(cnxx, po_number):
    sql = (
        "SELECT C.DOC_NAME, C.PROJECT_NO, sum(A.qty*B.unit_price)"
        "FROM [ETI].[dbo].[P_ORDER_SUBDTL] A "
        "inner join p_order_dtl B on B.ITEM_NO = A.ITEM_NO "
        "inner join projet C on C.PROJECT_NO = LEFT(A.job_no,4) "
        "where A.po={} and B.po={} and b.SELECTED_ITEM=1"
        "group by C.DOC_NAME, C.PROJECT_NO"
        .format(po_number, po_number)
    )
    df = pd.read_sql(sql, cnxx)
    return df


def save_to_excel(df, save_path):
    writer = pd.ExcelWriter(save_path)
    df.to_excel(writer, sheet_name='sheet11', index=False)
    writer.save()


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
