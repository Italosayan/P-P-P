from flask import Flask, render_template, url_for, request, flash, redirect, session, jsonify
import pandas as pd

'''
NOTE: Make sure "sepp-sample.csv" is in the same
directory as this file. Make sure column names for latitude
and longitude are the same as listed in the homepage method.
'''
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def homepage():
    try:
        # Read in Crime data
        df = pd.read_csv("sepp-sample.csv")
        # Grab subset of columns, just latitude and longitude
        df = df[["LATITUDE", "LONGITUDE", "score"]]
        # Turn dataframe into list of latitude and longitude pairs
        data_in = df.values.tolist()

        return render_template("index.html", data_in=data_in)
    except:
        print("error launching app")


if __name__ == "__main__":
    app.secret_key = "super secret key"
    app.config["SESSION_TYPE"] = "filesystem"
    app.run(debug=True)
