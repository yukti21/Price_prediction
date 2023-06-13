import pandas as pd
import sqlite3
import sqlalchemy

try:
    conn = sqlite3.connect(r'predidb1.db')
except Exception as e:
    print(e)

#Now in order to read in pandas dataframe we need to know table name
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#print(f"Table Name : {cursor.fetchall()}")

df = pd.read_sql_query('SELECT * FROM Record', conn)
conn.close()
type(df.iat[0,1])
print(df.dtypes)
print(df)
