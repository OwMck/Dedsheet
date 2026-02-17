import pandas as pd


# Reads excel sheet into a pandas dataframe and head shows top of spreadsheet
#df = pd.read_excel("sales_data.xlsx", engine="openpyxl")
#print(df.head())


from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    df_preview = None

    if request.method == 'POST':
        # Check if file was uploaded
        if 'spreadsheet' not in request.files:
            return "No file part"

        file = request.files['spreadsheet']

        if file.filename == '':
            return "No selected file"

        # Detect file type and read into pandas
        ext = file.filename.split('.')[-1].lower()
        if ext in ['xls', 'xlsx']:
            df = pd.read_excel(file)
        elif ext == 'csv':
            df = pd.read_csv(file)
        else:
            return "Unsupported file type"

        # Prepare a preview of the first few rows
        df_preview = df.head().to_html()

    return render_template('/website/home.html', df_preview=df_preview)

if __name__ == "__main__":
    app.run(debug=True)
