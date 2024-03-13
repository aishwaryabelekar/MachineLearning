# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 00:02:11 2024

@author: abelekar
"""

import pandas as pd
import pyodbc

def export_tables_to_excel(access_file_path, output_folder):
    # Set up the connection to MS Access using pyodbc
    conn_str = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={access_file_path};'
    conn = pyodbc.connect(conn_str)

    # Create a cursor to execute SQL queries
    cursor = conn.cursor()

    # Get the table names from the database
    table_query = cursor.tables(tableType='TABLE')
    table_names = [table.table_name for table in table_query]

    # Iterate over each table and export to Excel
    for table_name in table_names:
        query = f'SELECT * FROM [{table_name}]'
        df = pd.read_sql(query, conn)

        # Save the DataFrame to an Excel file
        excel_file_path = f'{output_folder}/{table_name}.xlsx'
        df.to_excel(excel_file_path, index=False)
        print(f'Table {table_name} exported to {excel_file_path}')

    # Close the database connection
    conn.close()

# Replace 'path\to\your\database.accdb' with the actual path to your MS Access database
access_file_path = r'C:\Users\abelekar\Documents\RA_CERTTFiles\Team_101_Mission_1_CERTT_Output.accdb'

# Replace 'path\to\your\output\folder' with the desired folder to save Excel files
output_folder = r'C:\Users\abelekar\Documents\RA_CERTTFiles\ConvertedFiles'

# Run the export function
export_tables_to_excel(access_file_path, output_folder)
