# In[1]:
import pandas as pd
import requests
import urllib3

urllib3.disable_warnings()

# In[4]:
# url1 = input('Enter url here: ')
url1 = 'http://www.itsec.gov.cn/cp/cpgg/201204/t20120401_14829.html'
response = requests.get(url1, verify=False)
response.encoding = response.apparent_encoding
print(response)

# In[5]:
html = response.text
# print(html)

# In[7]:
tb = pd.read_html(html, header=0)[0]
# meta = tb.pop("序号").to_frame()
print(tb)

# print(tb.columns.tolist())
#
# cols = "`,`".join([str(i) for i in tb.columns.tolist()])
#
# print(cols)
# for i,row in tb.iterrows():
#     print(row)
#     print(len(row))

# In[8]:
# for i in range(len(tb)):
#     print(tb.iloc[i,:])

