import datetime
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn
#
# @app.route('/')
# def index():
#     conn = get_db_connection()
#     posts = conn.execute('SELECT * FROM posts').fetchall()
#     conn.close()
#     return render_template('index.html', posts=posts)

@app.route('/')
def hello():
    return render_template('index.html', utc=datetime.datetime.utcnow())

@app.route('/about/')
def about():
    return '<h4>This is a Flask web application.</h4>'

@app.route('/mesaje/')
def mesaje():
    mesaje = ['Primul mesaj.',
                'Al doilea mesaj.',
                'Al treilea mesaj.',
                'Al patrulea mesaj.'
                ]

    return render_template('mesaje.html', mesaje=mesaje)


if __name__ == '__main__':
    app.run()