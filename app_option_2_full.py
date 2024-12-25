########## Lab work №6 (05.12.2024) ##########


# Task 1

# Option 2
from flask import Flask, render_template
import sqlite3

conn = sqlite3.connect("musics.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM musics")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


app = Flask(__name__)


def get_music():
    conn = sqlite3.connect("musics.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM musics")
    rows = cursor.fetchall()
    conn.close()
    return rows


@app.route("/")
def index():
    musics = get_music()
    return render_template("index_musics.html", musics=musics)


if __name__ == "__main__":
    app.run(debug=True)
