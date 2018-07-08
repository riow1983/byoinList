import sqlite3
import pandas as pd

excel_name = "HOSP2017-2.xlsx"
filename="ihep"

con=sqlite3.connect(filename+".db")

wb = pd.ExcelFile(excel_name)
sheet = wb.sheet_names[0]

df = pd.read_excel(excel_name, sheet_name=sheet)
df.to_sql(sheet, con, index=False, if_exists="replace")
con.commit()
con.close()
