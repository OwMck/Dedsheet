# https://www.datacamp.com/tutorial/pandas-profiling-ydata-profiling-in-python-guide
# pip install ydata-profiling

import pandas as pd
from ydata_profiling import ProfileReport

df= pd.read_excel("sales_data.xlsx")
profile= ProfileReport(df, title="TestReport")

profile.to_notebook_iframe()

##Doesn't work for now, potential issue with packages inside my VENV