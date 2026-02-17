import pandas as pd


#Reads excel sheet into a pandas dataframe and head shows top of spreadsheet
df = pd.read_excel("sales_data.xlsx", engine="openpyxl")
print(df.head())
