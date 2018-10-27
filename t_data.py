from flask import Flask, render_template, session, request, flash, url_for, redirect
from db import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///tut.db', echo=False)

Session = sessionmaker(bind=engine)
dennis = Session()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['std_id'] == 'PS/CSC/15/0004':
    
            session['logged_in'] = True
            print('You are loged in')
            return redirect(url_for('vote'))
        else:
            error = 'Invalid'
    return render_template('login.html', error = error)
    
        

@app.route('/login', methods=['POST'])
def login():
    STUDENTS_ID = str(request.form['std_id'])

    query = dennis.query(Students).filter(Students.std_id.in_([STUDENTS_ID]))
    result = query.first()
    # if request.form['std_id'] == 'PS/CSC/15/0000':    #hard coded data
    if result:  
        session['logged_in'] = True
    else:
        print('Massa you have wrong data. Register')
    return index()




@app.route('/admin', methods=['GET','POST'])  #i thought it would be POST only but when you are trying in the browser, you are getting :)
def admin():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['std_id']:
            print('Massa fill in the forms')
        else:
            data = Students(
                        request.form['name'],
                        request.form['std_id'],
                    )
            dennis.add(data)
            dennis.commit()
            print('Data Successfully added')
    return render_template('/admin.html')
       

    

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You are logged out')
    return(redirect(url_for('index')))
    

@app.route('/vote')
def vote():
    # return render_template(url_for('logout'))
    return render_template('vote.html')


if __name__ == '__main__':
    app.secret_key = b'haha... its a generated key' # i had an error when i was running the app i guess we can use another secured method
    app.run(debug=True, port=7000)