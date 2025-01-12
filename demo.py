import pandas as pd
import openpyxl
import sqlalchemy as sa
import pyodbc

df = pd.read_excel('C:\\Users\\ZBook 15\\Desktop\\employeedata.xlsx')
df["FullName"] = df["FirstName"] + " " + df["LastName"]
print(df)

engine = sa.create_engine('mssql://./DESKTOP-CVG0O1Q/datawarehouse?driver=SQL+Server+Native+Client+11.0')

df.to_sql('employee', engine, if_exists='fail', index=False)