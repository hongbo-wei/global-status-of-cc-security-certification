import pandas as pd
import pymysql

''' 
数据来源去CC官网数据下载认证产品的.csv文件
https://www.commoncriteriaportal.org/products/
Download CSV
'''

# File path to the CSV file
csv_file_path = "database/itsec_ch.csv"

# Read the CSV file into a DataFrame object
# encoding to avoid error
# "UnicodeDecodeError: 'utf-8' codec can't decode byte 0xae in position 2981: invalid start byte"
df = pd.read_csv(csv_file_path)

meta = df.pop('id').to_frame()

# Add a column with default value
df["scheme"] = 'CH'

# set null column value to none
df = df.where(df.notnull(), None)

# Print the DataFrame
print(df)

# Connect to the database
connection = pymysql.connect(
            host="localhost",
            user='root',
            password='KeepLearning',
            database='cc_statistic',)
cursor = connection.cursor()

table_name = 'certified_products_1'

# Alter table auto_increment ID number
cursor.execute(f'ALTER TABLE {table_name} AUTO_INCREMENT=1')

# creating column list for insertion
cols = "`,`".join([str(i) for i in df.columns.tolist()])

# Insert DataFrame records one by one.
for i, row in df.iterrows():
    sql = f"INSERT INTO {table_name} (`" + cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))

    # the connection is not auto-committed by default, so we must commit to save our changes
    connection.commit()

connection.close()