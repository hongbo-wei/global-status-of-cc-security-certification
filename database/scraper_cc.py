import pandas as pd
import pymysql

''' 
数据来源去CC官网数据下载认证产品的.csv文件
https://www.commoncriteriaportal.org/products/
Download CSV
'''

# File path to the CSV file
csv_file_path = "database/csv/certified_products.csv"

# Read the CSV file into a DataFrame object
# encoding to avoid error
# "UnicodeDecodeError: 'utf-8' codec can't decode byte 0xae in position 2981: invalid start byte"
df = pd.read_csv(csv_file_path, encoding="iso-8859-1")

# set null column value to none
df = df.where(df.notnull(), None)

df = df.rename(columns = {
    'Category': 'category',
    'Name': 'name',
    'Manufacturer': 'manufacturer',
    'Scheme': 'scheme',
    'Assurance Level': 'assurance_level',
    'Protection Profile(s)': 'protection_profile',
    'Certification Date': 'certification_date',
    'Archived Date': 'archived_date',
    'Certification Report URL': 'certification_report_url',
    'Security Target URL': 'security_target_url',
    'Maintenance Date': 'maintenance_date',
    'Maintenance Title': 'maintenance_title',
    'Maintenance Report': 'maintenance_report',
    'Maintenance ST': 'maintenance_st',
    })

# Print the DataFrame
print(df)

# Connect to the database
connection = pymysql.connect(
            host="localhost",
            user='root',
            password='KeepLearning',
            database='cc_statistic',)
cursor = connection.cursor()

table_name = 'certified_products'

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