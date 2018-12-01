from flask import Flask
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def result():
    k = 'Kwame Onions'
    con = sql.connect('polls.db')
    c = con.cursor()
    c.execute("SELECT votes from students WHERE name=?",(k,) )
    y = c.fetchone()
    print(y)
    return 'Hello'


if __name__ == '__main__':
    # app.secret_key = b'haha... its a generated key' # i had an error when i was running the app i guess we can use another secured method
    # images = Images(app)
    app.run(debug=True, port=8000)