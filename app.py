# cheatsheet.nz
# November 2020

import sqlite3

from flask import Flask, render_template

app = Flask(__name__)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route("/")
def index():
    conn = sqlite3.connect('./data/cheatsheet.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    sheet = c.execute('SELECT * FROM sheet').fetchall()
    category = c.execute('SELECT * FROM category').fetchall()
    content = c.execute('SELECT * FROM content ORDER BY content_title').fetchall()
    conn.close()

    return render_template("cheatsheet.html", sheet=sheet, category=category, content=content)

if __name__ == "__main__":
    app.run(debug=True)