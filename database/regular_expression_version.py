import requests
from bs4 import BeautifulSoup
import re
from mysql.connector import connect

def creat():
    conn = connect(
        host="localhost",
        user='root',
        password='haha',
        database='test',)

    sql = '''CREATE TABLE `chinadb` (
            `id` INT NOT NULL AUTO_INCREMENT,
            'No' INT NULL,
            `company` VARCHAR(45) NULL,
            `product` VARCHAR(45) NULL,
            `certification_No.` VARCHAR(45) NULL,
            `level` VARCHAR(45) NULL,
            `date_of_issue` VARCHAR(45) NULL,
            `expiration_date` VARCHAR(45) NULL,
            PRIMARY KEY (`id`))
          ENGINE = InnoDB
          DEFAULT CHARACTER SET = utf8;
         '''

    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.execute('CHARACTER SET = utf8')
    conn.close()
    print('Done')

def insert(value):
    db = connect(host='localhost', user='root', password='haha', database='test')

    cursor = db.cursor()
    sql = '''
    INSERT INTO chinadb(company, product, certification_No, level, date_of_issue, expiration_date) 
    VALUES (%s, %s, %s, %s, %s, %s)
    '''
    try:
        cursor.execute(sql, value)
        db.commit()
        print('插入数据成功')
    except:
        db.rollback()
        print("插入数据失败")
    db.close()


def parseweb(weburl):
    req = requests.get(weburl)
    req.encoding = 'utf-8'

    bs = BeautifulSoup(req.text, 'html.parser')
    ccdata = bs.find_all('tbody')
    ccdata.encoding = 'utf-8'
    ccdata = str(ccdata)

    # re匹配需要的数据
    info_1 = re.compile('''<tr>
.*
<td.*?>(.*?)</td>
<td.*?>(.*?)</td>
<td.*?>(.*?)</td>
<td.*?>(.*?)</td>
<td.*?>(.*?)</td>
<td.*?>(.*?)</td>
</tr>''')

    items = re.findall(info_1, ccdata)
    for stuff in items[1:]:
        print(stuff)
        insert(stuff)

# reset the value of the AUTO_INCREMENT attribute
conn = connect(
host="localhost",
user='root',
password='haha',
database='test',)

cursor = conn.cursor()
cursor.execute('ALTER TABLE chinadb AUTO_INCREMENT=161')

# re匹配需要的数据
url = input('Enter ITSEC url: ')
res = requests.get(url)
res.encoding = 'utf-8'
# print(res.status_code)

soup = BeautifulSoup(res.text, 'html.parser')
data = soup.find_all('ul')
data.encoding = 'utf-8'
data = str(data)

# re匹配需要的数据
info = re.compile('<li><a href=".(.*?)" .*title.*</li>')

prefix = 'http://www.itsec.gov.cn/cp/cpgg'
item = re.findall(info, data)

for i in item:
    web = prefix + i
    print(web)



