########## Lab work №6 (05.12.2024) ##########


# Task 1

# Option 1
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_presents():
    conn = sqlite3.connect("presents.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM presents")
    rows = cursor.fetchall()
    conn.close()
    return rows


@app.route("/")
def index():
    presents = get_presents()
    return render_template("index.html", presents=presents)


if __name__ == "__main__":
    app.run(debug=True)
