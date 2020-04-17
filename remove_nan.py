import pandas as pd


df = pd.read_csv("database.csv", dtype=str)
#or if excel file
#df = pd.read_excel("filename", dtype=str)

df = df[pd.notnull(df['pixels'])]

df.to_csv("newfile.csv"); 
