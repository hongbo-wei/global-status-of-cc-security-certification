import requests
import re
import pymysql
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path

"""
This script is to populate the 'scheme' column
"""
# re匹配需要的数据
url = 'https://www.niap-ccevs.org/Product/PCL.cfm'
res = requests.get(url)
res.encoding = 'utf-8'
print(res.status_code)

soup = BeautifulSoup(res.text, 'html.parser')

# How to use BeautifulSoup finding a specific tag: .find_all(tag, {attribute})
data = soup.find_all('table', {'class': "tablesorter"})
data.encoding = 'utf-8'
data = str(data)
# print(data)

# Next step, use regular expression to find Scheme info
scheme = re.compile('<img.*?title="(.*?)"')
schemes = re.findall(scheme, data)

# # Write data into an HTML file
# path = Path('database/niap.html')
# path.write_text(data)

# Find the column product for matching up
tables = pd.read_html('database/niap.html')
df = tables[0]  # Save first table in variable df1

df = df.rename(columns = {
    'Product': 'name',
    'VID': 'vid',
    'Conformance Claim': 'conformance_claim',
    'CCTL': 'cctl',
    'Certification Date': 'certification_date',
    'Assurance Maintenance Date': 'archived_date',
    'Scheme': 'scheme'
    })

print(df)
# for padas: specific column df['name']

connection = pymysql.connect(
    host="localhost",
    user='root',
    password='KeepLearning',
    database='cc_statistic', )
cursor = connection.cursor()

table = 'certified_products'

# zip two lists to use them together
source = zip(schemes[0:], df['name'])
for i in source:
    # Update value
    sql = f'UPDATE {table} SET Scheme = "{i[0]}" WHERE name = "{i[1]}"'
    cursor.execute(sql)
    # Insert value
    # sql = 'INSERT INTO cc_statistic_niap(Scheme) VALUES (%s)'

connection.commit()
connection.close()
