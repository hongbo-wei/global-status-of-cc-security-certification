import pymysql
import pandas as pd
import requests
import urllib3

urllib3.disable_warnings()

'''
中国信息安全评测中心 http://www.itsec.gov.cn/cp/cpgg/
Copy table in MySQL: CREATE TABLE new_table AS SELECT * FROM old_table
没有等级认证的：通过国家信息安全产品型号认证。有的则为产品通过国家信息安全产品分级认证
'''

# Use a Flag
active = True
while active:
    url = input('Enter url: ')
    if url == 'quit':
        break

    response = requests.get(url, verify=False)
    response.encoding = response.apparent_encoding
    print(response)

    html = response.text

    df = pd.read_html(html, header=0)[0]
    meta = df.pop('序号').to_frame()    # to delete '序号' column

    # table head rename
    df = df.rename(columns = {
        '获证单位': 'manufacturer',
        '获证产品名称': 'name',
        '证书编号': 'certification_id',
        '级别': 'assurance_level',
        '发证日期': 'certification_date',
        '有效期': 'archived_date'
        })
    
    # Add a column with default value
    df["scheme"] = 'CH'

    # set null column value to none
    df = df.where(df.notnull(), None)
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
    cursor.execute(f'ALTER TABLE {table_name} AUTO_INCREMENT = 1')

    # creating column list for insertion
    cols = "`,`".join([str(i) for i in df.columns.tolist()])

    # Insert DataFrame records one by one.
    for i, row in df.iterrows():
        sql = f"INSERT INTO {table_name} (`" + cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
        cursor.execute(sql, tuple(row))

        # the connection is not auto-committed by default, so we must commit to save our changes
        connection.commit()

    connection.close()
