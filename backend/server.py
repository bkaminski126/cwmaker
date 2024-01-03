# Filename - server.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import math
import json

app = Flask(__name__)
CORS(app)

x = datetime.datetime.now()


# Route for seeing a data
@app.route("/data")
def get_time():
    # Returning an api for showing in  reactjs
    return {
        "Name": "geek",
        "Age": "22",
        "TESt": "xd",
        "Date": x,
        "programming": "python",
    }


@app.route("/validcw", methods=["GET", "POST"])
def check_validity():
    data = request.data.decode("utf-8")
    data = json.loads(data)
    cw = data['cw']

    # note: rotational symmetry CWs have palindromic ways to write in linear format, if they are square
    # for ch in range(len(cw)):
    #     if cw[ch] != "0":
    #         cw[ch] = "1"

    return {
        "isValid": len(cw) >= 16 and cw[::-1] == cw and math.sqrt(len(cw)).is_integer()
    }


# Running app
if __name__ == "__main__":
    app.run(port=8000, debug=False)
