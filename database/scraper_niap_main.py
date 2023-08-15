"""Title database Field name when scraping, Django class user lowercase"""
import pymysql
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pathlib import Path

"""
This Section should be used to write data into html file
After read the .cfm page, wrtie the innerHTML part of <th>Certification Date</th> in niap.html
"""
######
# re匹配需要的数据
# url = 'https://www.niap-ccevs.org/Product/PCL.cfm' 
# # url = input('Enter url: ')
# res = requests.get(url)
# res.encoding = 'utf-8'
# print(res.status_code)

# soup = BeautifulSoup(res.text, 'html.parser')

# # How to use BeautifulSoup finding a specific tag: .find_all(tag, {attribute})
# data = soup.find_all('table', {'class': "tablesorter"})
# data.encoding = 'utf-8'
# data = str(data)
# # print(data)


# # Write data into an HTML file
# path = Path('database/niap.html')
# path.write_text(data)
######

# set the table
tables = pd.read_html('database/niap.html')
df = tables[0]  # Save first table in variable df1
print(df)

df = df.rename(columns = {
    'Product': 'name',
    'VID': 'vid',
    'Conformance Claim': 'conformance_claim',
    'CCTL': 'cctl',
    'Certification Date': 'certification_date',
    'Assurance Maintenance Date': 'archived_date',
    'Scheme': 'scheme'
    })

meta = df.pop("scheme").to_frame()
meta = df.pop("vid").to_frame()
# df = df.where(pd.notnull(df), None)
df = df.fillna('None')

# creating column list for insertion
cols = "`,`".join([str(i) for i in df.columns.tolist()])
print(cols)

# Connect to the database
connection = pymysql.connect(
            host="localhost",
            user='root',
            password='KeepLearning',
            database='cc_statistic',)
cursor = connection.cursor()

table = 'certified_products'
# Alter table auto_increment ID number
cursor.execute(f'ALTER TABLE {table} AUTO_INCREMENT=1')

# Insert DataFrame records one by one.
for i, row in df.iterrows():

    print(i, row)
    sql = f"INSERT INTO {table} (`" + cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    print(sql)
    cursor.execute(sql, tuple(row))

    # the connection is not auto-committed by default, so we must commit to save our changes
    connection.commit()  

connection.close()
