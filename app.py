from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect
from db import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from werkzeug import secure_filename
# from flask_images import resized_img_src, Images
import json, os

engine = create_engine('sqlite:///tut.db', echo=False)

Session = sessionmaker(bind=engine)
dennis = Session()

app = Flask(__name__)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for('vote'))
        # return ("Welcome here <a href='/logout'> Logout</a>")



@app.route('/login', methods=['POST'])
def login():
    STUDENTS_ID = str(request.form['std_id'])

    query = dennis.query(Students).filter(Students.std_id.in_([STUDENTS_ID]))
    result = query.first()
    # if request.form['std_id'] == 'PS/CSC/15/0000':    #hard coded data
    if result:  
        session['logged_in'] = True
    else:
        flash('Massa you have wrong data. Register')
        # print('Massa you have wrong data. Register')
        # tryout a redirect to an authorised error page
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
                        request.form['hall_of_residence'],
                        request.form['wing'],
                    )
            dennis.add(data)
            dennis.commit()
            print('Data Successfully added')
    return render_template('/admin.html')
       

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return index()


@app.route('/vote', methods=['GET', 'POST'])
def vote():
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['President']['role']
        name = data['President']['name']
        img = data['President']['images']

    if request.method == 'POST':
        vote = request.form['like']   #do a scheck on the when the user selects none
        print('Voted for', vote)
        return redirect(url_for('sec'))   #this is where the logic for solving the hall and wings problem will be about. Here we can use a switch case or a simple if-else
    return render_template('vote.html', role=role, img=img, name=name)

    # return render_template(url_for('logout'))


@app.route('/sec', methods=['GET', 'POST'])
def sec():
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Secretary']['role']
        name = data['Secretary']['name']
        img = data['Secretary']['images']

    if request.method == 'POST':
         vote = request.form['like']
         print('Voted for', vote)
    return render_template('vote.html', role= role, name=name, img=img)




if __name__ == '__main__':
    app.secret_key = b'haha... its a generated key' # i had an error when i was running the app i guess we can use another secured method
    # images = Images(app)
    app.run(debug=True, port=8000)