from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_gifts():
    conn = sqlite3.connect('gifts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gifts")
    gifts = cursor.fetchall()
    conn.close()
    return gifts

@app.route('/')
def index():
    gifts = get_gifts()
    return render_template('index.html', gifts=gifts)

if __name__ == '__main__':
    app.run(debug=True)