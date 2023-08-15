import pandas as pd

tables = pd.read_html('niap.html')

df = tables[0]  # Save first table in variable df1
# df[['Product','Company']] = df['Product'].str.split('Inc.',expand=True)

print(df)

