import sqlite3
import pandas as pd

# db
dbname = "ihep.db"

# db connect
conn = sqlite3.connect(dbname)

# read db as pandas dataframe
df = pd.read_sql("SELECT * FROM HOSP2017", conn)

print(df)