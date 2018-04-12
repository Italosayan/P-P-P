from flask import Flask, render_template, url_for, request, flash, redirect, session, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def homepage():
    try:
        # Read in Crime data
        df = pd.read_csv("crimedata.csv")
        # Grab subset of columns, just latitude and longitude
        df = df[["LATITUDE", "LONGITUDE"]]
        # Turn dataframe into list of latitude and longitude pairs
        data_in = df.values.tolist()
        
        return render_template("index.html", data_in=data_in)
    except:
        print("error launching app")

if __name__ =="__main__":
    app.secret_key = "super secret key"
    app.config["SESSION_TYPE"] = "filesystem"
    app.run(debug=True)
