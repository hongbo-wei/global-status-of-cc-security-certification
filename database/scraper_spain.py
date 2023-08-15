import pymysql
import pandas as pd
import requests
import urllib3

urllib3.disable_warnings()

# Use a Flag
# while True:
url = 'https://oc.ccn.cni.es/en/certified-products/certified-products'

# url = input('Enter url or quit: ')
# if url == '':
#     url = 'https://oc.ccn.cni.es/en/certified-products/certified-products'
# if url == 'quit':
#     break

response = requests.get(url, verify=False)
response.encoding = response.apparent_encoding
print(response)

html = response.text

df = pd.read_html(html, header=0)[0]

# Set empty value to None
df = df.where(df.notnull(), None)

# Delete specific rows
df = df.iloc[::2]

# Reset index
df = df.reset_index(drop=True)

# Pop the last column, because there is only NaN in it.
df.pop("Certification Date")

# Rename a column so that we can store the info into MySQL
df = df.rename(columns={
    'Name': 'name',
    'Manufacturer': 'manufacturer',
    'Category': 'category',
    'Evaluation start date': 'certification_date',
    })

df["scheme"] = 'ES'
# df = df.fillna('None')
print(df)

# check the name of columns
# for col in df.columns:
#     print(col)


# Connect to the database
connection = pymysql.connect(
            host="localhost",
            user='root',
            password='KeepLearning',
            database='cc_statistic',)
cursor = connection.cursor()

table_name = 'certified_products'

# creating column list for insertion
cols = "`,`".join([str(i) for i in df.columns.tolist()])

# Insert DataFrame records one by one without dupliacation.
for i, row in df.iterrows():

    # Reset table auto_increment ID number
    cursor.execute(f'ALTER TABLE {table_name} AUTO_INCREMENT = 1')

    # INSERT IGNORE INTO table for updating table without duplciating data
    # CAUTION! This only works as that column has UNIQUE attribute, UNIQUE only allows a name appear once
    sql = f"INSERT INTO {table_name} (`" + cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))

    # the connection is not auto-committed by default, so we must commit to save our changes
    connection.commit()

# Delete extra text
sql = f"UPDATE {table_name} SET certification_date = replace(certification_date,'Certification Date ','');"
cursor.execute(sql)

sql = f"UPDATE {table_name} SET certification_date = replace(certification_date,' None','');"
cursor.execute(sql)

connection.commit()
connection.close()
