# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 23:58:22 2024

@author: abelekar
"""

import pandas as pd
import pyodbc

# Set up the connection to MS Access
conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\abelekar\Documents\RA_CERTTFiles\Team_101_Mission_1_CERTT_Output.accdb;'
conn = pyodbc.connect(conn_str)

# Replace 'your_table_name' with the actual table name in your MS Access database
query = 'SELECT * FROM Mission_1_ALARMS'

# Fetch data into a pandas DataFrame
df = pd.read_sql(query, conn)

# Close the database connection
conn.close()

# Save the DataFrame to an Excel file
excel_file_path = r'C:\Users\abelekar\Documents\RA_CERTTFiles\ConvertedFiles\file.xlsx'
df.to_excel(excel_file_path, index=False)

print(f'Data successfully exported to {excel_file_path}')
