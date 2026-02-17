import pandas as pd
from distutils.log import debug
from fileinput import filename
from flask import Flask, request, render_template
print(render_template)
app = Flask(__name__) 

# Reads excel sheet into a pandas dataframe and head shows top of spreadsheet
#df = pd.read_excel("sales_data.xlsx", engine="openpyxl")
#print(df.head())

# https://www.geeksforgeeks.org/python/how-to-upload-file-in-python-flask/
@app.route('/')  
def main():  
    return render_template("home.html")  

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(f.filename)  
        return render_template("acknowledge.html", name = f.filename)  

if __name__ == '__main__':  
    app.run(debug=True)  

