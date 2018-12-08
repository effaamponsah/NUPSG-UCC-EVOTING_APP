from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response
from db import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json, os
from error import msg
from time import sleep

import sqlite3 as sql

wing_name=''
wing_name2=''
hall=''
c_residence=''


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
    has_voted = False
    STUDENTS_ID = str(request.form['std_id']).upper()

    print(STUDENTS_ID)
    query = dennis.query(Students).filter(Students.std_id.in_([STUDENTS_ID]))
    result = query.first()
    # if request.form['std_id'] == 'PS/CSC/15/0000':    #hard coded data
    if result:  
        session['logged_in'] = True
        has_voted = True
        new_stamp = request.cookies.get(STUDENTS_ID)

        #####################################
        #fetch for some details based on the index number provided
        con = sql.connect('tut.db')
        c = con.cursor()
        c.execute("SELECT wing from students WHERE index_no=:k", {"k": STUDENTS_ID})
        y = c.fetchone()
        w = y[0]
        global wing_name
        wing_name = w
        sleep(0.2)

        c.execute("SELECT hall_of_affiliation from students WHERE index_no=:k", {"k": STUDENTS_ID})
        y = c.fetchone()
        w = y[0]
        global hall
        hall = w
        sleep(0.2)

        c.execute("SELECT current_residence from students WHERE index_no=:k", {"k": STUDENTS_ID})
        y = c.fetchone()
        w = y[0]
        global c_residence
        c_residence = w
        sleep(0.2)

        c.execute("SELECT wing2 from students WHERE index_no=:k", {"k": STUDENTS_ID})
        y = c.fetchone()
        w = y[0]
        global wing_name2
        wing_name2 = w

        #####################################
        if new_stamp:
            print('Has voted as ', new_stamp)
            return redirect(url_for('error'))
        else:
            print("Wing name",wing_name)
            print("Second wing name",wing_name2)
            print("Hall",hall)
            print("Residence",c_residence)
            print('Hasnt voted')

    else:
        flash('Please check wether you entered the correct index number')
        # print('Massa you have wrong data. Register')
        # tryout a redirect to an authorised error page

    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('userId', STUDENTS_ID)


    if has_voted:
        new_stamp = 'Dennis'
        print('set cookie')
        resp.set_cookie(STUDENTS_ID, new_stamp)
    return resp


@app.route('/admin', methods=['GET','POST'])  #i thought it would be POST only but when you are trying in the browser, you are getting :)
def admin():
    if request.method == 'POST':
        ID = str(request.form['std_id']).upper()
        if not request.form['name'] or not request.form['std_id']:
            print('Massa fill in the forms')
        else:
            data = Students(
                        request.form['name'],
                        request.form['res'],
                        ID,
                        request.form['hall_of_affiliation'],
                        request.form['wing'],
                        request.form['wing2'],
                    )
            dennis.add(data)
            dennis.commit()
            print('Data Successfully added')
            return  '''
                <h2>Data Successfully added</h2>
                <a href='/admin'>Go back</a>
            '''
    return render_template('/admin.html')
       

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return index()


@app.route('/pres', methods=['GET', 'POST'])
def vote():
    pres_vt = sql.connect('polls.db')
    v = pres_vt.cursor()
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['President']['role']
        name = data['President']['name']
        img = data['President']['images']

    if request.method == 'POST':
        vote = request.form['like']   #do a check on the when the user selects none
        if vote == '':
            print('User never choose anyone to vote for')
            
        v.execute("UPDATE president SET votes =votes+?  WHERE name= ?", (1,vote,))
        pres_vt.commit()
        print('Voted for', vote)
        return redirect(url_for('sec'))   #this is where the logic for solving the hall and wings problem will be about. Here we can use a switch case or a simple if-else
    return render_template('pres.html', role=role, img=img, name=name)

    # return render_template(url_for('logout'))


@app.route('/sec', methods=['GET', 'POST'])
def sec():
    pres_vt = sql.connect('polls.db')
    v = pres_vt.cursor()
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Secretary']['role']
        name = data['Secretary']['name']
        img = data['Secretary']['images']

    if request.method == 'POST':
         vote = request.form['like']
         v.execute("UPDATE secretary SET votes =votes+?  WHERE name= ?", (1,vote,))
         pres_vt.commit()
         print('Voted for', vote)
         return redirect(url_for('org'))  
    return render_template('sec.html', role= role, name=name, img=img)


@app.route('/org', methods=['GET', 'POST'])
def org():
    pres_vt = sql.connect('polls.db')
    v = pres_vt.cursor()
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Organizing-Secretary']['role']
        name = data['Organizing-Secretary']['name']
        img = data['Organizing-Secretary']['images']

    if request.method == 'POST':
         vote = request.form['like']
         v.execute("UPDATE organizing_sec SET votes =votes+?  WHERE name= ?", (1,vote,))
         pres_vt.commit()
         print('Voted for', vote)
         return redirect(url_for('welfare'))  
    return render_template('org.html', role= role, name=name, img=img)


@app.route('/welfare', methods=['GET', 'POST'])
def welfare():
    pres_vt = sql.connect('polls.db')
    v = pres_vt.cursor()
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Welfare-Chairperson']['role']
        name = data['Welfare-Chairperson']['name']
        img = data['Welfare-Chairperson']['images']

    if request.method == 'POST':
         vote = request.form['like']
         v.execute("UPDATE welfare_chair SET votes =votes+?  WHERE name= ?", (1,vote,))
         pres_vt.commit()
         print('Voted for', vote)
         return redirect(url_for('p_sec'))  
    return render_template('welfare.html', role= role, name=name, img=img)


@app.route('/p_sec', methods=['GET', 'POST'])
def p_sec():
    pres_vt = sql.connect('polls.db')
    v = pres_vt.cursor()
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Prayer-Secretary']['role']
        name = data['Prayer-Secretary']['name']
        img = data['Prayer-Secretary']['images']

    if request.method == 'POST':
         vote = request.form['like']
         v.execute("UPDATE prayer_sec SET votes =votes+?  WHERE name= ?", (1,vote,))
         pres_vt.commit()
         print('Voted for', vote)

         ##################################
         #this is where the breakthrough is
         if wing_name == 'Organizers':
             return redirect(url_for('cs')) 
         elif wing_name == 'Sch.Cord':
             return redirect(url_for('sc')) 
         elif wing_name == 'Evangelism':
             return redirect(url_for('evang')) 
         elif wing_name == 'Choir':
             return redirect(url_for('choir')) 
         else:
             return redirect(url_for('hall_name'))  
            #  return redirect(url_for('welfare')) 
             
    return render_template('p_sec.html', role= role, name=name, img=img, wing_name=wing_name)

@app.route('/cs', methods=['GET', 'POST'])
def cs():
    pres_vt = sql.connect('polls.db')
    v = pres_vt.cursor()
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Chapel-Steward']['role']
        name = data['Chapel-Steward']['name']
        img = data['Chapel-Steward']['images']

    if request.method == 'POST':

        vote = request.form['like']
        v.execute("UPDATE chapel_steward SET votes =votes+?  WHERE name= ?", (1,vote,))
        pres_vt.commit()
        print('Voted for', vote)

        ############################
        if wing_name2 == 'Sch.Cord':
            return redirect(url_for('sc'))
        elif wing_name2 == 'Evangelism':
             return redirect(url_for('evang')) 
        elif wing_name2 == 'Choir':
             return redirect(url_for('choir')) 
        else:
             return redirect(url_for('hall_name'))
        ###########################
        return redirect(url_for('hall_name'))           
    return render_template('cs.html', role= role, name=name, img=img)


@app.route('/sc', methods=['GET', 'POST'])
def sc():
    pres_vt = sql.connect('polls.db')
    v = pres_vt.cursor()
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Schools Coordinator']['role']
        name = data['Schools Coordinator']['name']
        img = data['Schools Coordinator']['images']

    if request.method == 'POST':
         vote = request.form['like']
         v.execute("UPDATE sch_cord SET votes =votes+?  WHERE name= ?", (1,vote,))
         pres_vt.commit()
         print('Voted for', vote)
         
         
         ########################################
         if wing_name2 == 'Organizers':
             return redirect(url_for('cs'))
         elif wing_name2 == 'Evangelism':
             return redirect(url_for('evang')) 
         elif wing_name2 == 'Choir':
             return redirect(url_for('choir')) 
         else:
             return redirect(url_for('hall_name'))

         #############################################3
         return redirect(url_for('hall_name'))  
    return render_template('sc.html', role= role, name=name, img=img, wing_name2=wing_name2)


@app.route('/evang', methods=['GET', 'POST'])
def evang():
    pres_vt = sql.connect('polls.db')
    v = pres_vt.cursor()
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Evangelism-Coordinator']['role']
        name = data['Evangelism-Coordinator']['name']
        img = data['Evangelism-Coordinator']['images']

    if request.method == 'POST':
         vote = request.form['like']
         v.execute("UPDATE evang_cord SET votes =votes+?  WHERE name= ?", (1,vote,))
         pres_vt.commit()
         print('Voted for', vote)
         
         ######################
         if wing_name2 == 'Organizers':
             return redirect(url_for('cs'))
         elif wing_name2 == 'Sch.Cord':
             return redirect(url_for('sc')) 
         elif wing_name2 == 'Choir':
             return redirect(url_for('choir')) 
         else:
             return redirect(url_for('hall_name'))


         ######################
         return redirect(url_for('hall_name'))  
    return render_template('evang.html', role= role, name=name, img=img, wing_name2=wing_name2)


@app.route('/choir', methods=['GET', 'POST'])
def choir():
    pres_vt = sql.connect('polls.db')
    v = pres_vt.cursor()
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Choir-President']['role']
        name = data['Choir-President']['name']
        img = data['Choir-President']['images']

    if request.method == 'POST':
         vote = request.form['like']
         v.execute("UPDATE choir_president SET votes =votes+?  WHERE name= ?", (1,vote,))
         pres_vt.commit()
         print('Voted for', vote)
         
         ######################
         if wing_name2 == 'Organizers':
             return redirect(url_for('cs'))
         elif wing_name2 == 'Sch.Cord':
             return redirect(url_for('sc')) 
         elif wing_name2 == 'Evangelism':
             return redirect(url_for('evang'))
         else:
             return redirect(url_for('hall_name'))

         ######################
         return redirect(url_for('hall_name'))  
    return render_template('choir.html', role= role, name=name, img=img, wing_name2=wing_name2)


@app.route('/hall', methods=['GET', 'POST'])
def hall_name():
    pres_vt = sql.connect('polls.db')
    v = pres_vt.cursor()
    global hall
    global c_residence
    print('Hall', hall)
    print('Current', c_residence)
    # if hall and c_residence == 'ATL':
    if hall == 'ATL':  
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['ATL-HALL']['role']
            name = data['ATL-HALL']['name']
            img = data['ATL-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            v.execute("UPDATE ATL_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
            pres_vt.commit()
            print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)
    elif hall == 'KNH':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['KNH-HALL']['role']
            name = data['KNH-HALL']['name']
            img = data['KNH-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            v.execute("UPDATE KNH_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
            pres_vt.commit()
            print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)
    elif hall == 'Valco':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Valco-HALL']['role']
            name = data['Valco-HALL']['name']
            img = data['Valco-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            v.execute("UPDATE Valco_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
            pres_vt.commit()
            print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)
    elif hall == 'Oguaa':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Oguaa-HALL']['role']
            name = data['Oguaa-HALL']['name']
            img = data['Oguaa-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            v.execute("UPDATE Oguaa_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
            pres_vt.commit()
            print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)
    elif hall == 'Casford':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Casford-HALL']['role']
            name = data['Casford-HALL']['name']
            img = data['Casford-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            v.execute("UPDATE Casford_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
            pres_vt.commit()
            print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)
    elif hall == 'SRC':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['SRC-HALL']['role']
            name = data['SRC-HALL']['name']
            img = data['SRC-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            v.execute("UPDATE SRC_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
            pres_vt.commit()
            print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)

    elif hall == 'PSI':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['SRC-HALL']['role']
            name = data['SRC-HALL']['name']
            img = data['SRC-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            v.execute("UPDATE SRC_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
            pres_vt.commit()
            print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)

    elif hall == 'Adehye':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Adehye-HALL']['role']
            name = data['Adehye-HALL']['name']
            img = data['Adehye-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            v.execute("UPDATE Adehye_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
            pres_vt.commit()
            print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)

    elif hall == 'SUPERANNUATION':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Superannuation-Hostel']['role']
            name = data['Superannuation-Hostel']['name']
            img = data['Superannuation-Hostel']['images']
        if request.method == 'POST':
            vote = request.form['like']
            v.execute("UPDATE Superannuation SET votes =votes+?  WHERE name= ?", (1,vote,))
            pres_vt.commit()
            print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)
    else:
        return redirect(url_for('done'))
    

@app.route('/res', methods=['GET', 'POST'])
def res_():
    pres_vt = sql.connect('polls.db')
    v = pres_vt.cursor()
    global c_residence
    if c_residence == 'KNH': 
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['KNH-HALL']['role']
            name = data['KNH-HALL']['name']
            img = data['KNH-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE KNH_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)
        
    elif c_residence == 'ATL':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['ATL-HALL']['role']
            name = data['ATL-HALL']['name']
            img = data['ATL-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE ATL_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)
        # return('You wil vote for ATL')

    elif c_residence == 'Oguaa':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Oguaa-HALL']['role']
            name = data['Oguaa-HALL']['name']
            img = data['Oguaa-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE Oguaa_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'Casford':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Casford-HALL']['role']
            name = data['Casford-HALL']['name']
            img = data['Casford-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE Casford_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'Valco':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Valco-HALL']['role']
            name = data['Valco-HALL']['name']
            img = data['Valco-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE Valco_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'SRC':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['SRC-HALL']['role']
            name = data['SRC-HALL']['name']
            img = data['SRC-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE SRC_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'PSI':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['SRC-HALL']['role']
            name = data['SRC-HALL']['name']
            img = data['SRC-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE SRC_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'Adehye':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Adehye-HALL']['role']
            name = data['Adehye-HALL']['name']
            img = data['Adehye-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE Adehye_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'SUPERANNUATION':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Superannuation-Hostel']['role']
            name = data['Superannuation-Hostel']['name']
            img = data['Superannuation-Hostel']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE Superannuation SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'Apewosika':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Apewosika']['role']
            name = data['Apewosika']['name']
            img = data['Apewosika']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE Apewosika SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'Kwaprow':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Kwaprow']['role']
            name = data['Kwaprow']['name']
            img = data['Kwaprow']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE Kwaprow SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

        
    elif c_residence == 'Amamoma':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Amamoma']['role']
            name = data['Amamoma']['name']
            img = data['Amamoma']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE Amamoma SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'Ayensu':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Amamoma']['role']
            name = data['Amamoma']['name']
            img = data['Amamoma']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE Amamoma SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    else:
        return('You are from somewhere maybe Space')

@app.route('/done')
def done():
    return render_template('done.html')


@app.route('/error')
def error():
    e = msg()
    return e


@app.route('/results')
def result():
    result = sql.connect('polls.db')
    f = result.cursor()
    f.execute("SELECT * from president")
    pres = f.fetchall()

    f.execute("SELECT SUM(votes) from president")
    s = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'president'", (s,))
    result.commit()
    if pres[0][1] > pres[1][1]:
        c_pres = pres[0][0]
    elif pres[0][1] == pres[1][1]:
        c_pres = 'A tie'
    else:
        c_pres = pres[1][0]



    f.execute("SELECT * from secretary")
    sec = f.fetchall()
    f.execute("SELECT SUM(votes) from secretary")
    a = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'secretary'", (a,))
    result.commit()

    if sec[0][1] > sec[1][1]:
        c_sec = sec[0][0]
    elif sec[0][1] == sec[1][1]:
        c_sec = 'A tie'
    else:
        c_sec = sec[1][0]


    f.execute("SELECT * from chapel_steward")
    cs = f.fetchall()
    f.execute("SELECT SUM(votes) from chapel_steward")
    n = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'chapel_steward'", (n,))
    result.commit()

    if cs[0][1] > cs[1][1]:
        c_cs = cs[0][0]
    elif cs[0][1] == cs[1][1]:
        c_cs = 'A tie'
    else:
        c_cs = cs[1][0]

    f.execute("SELECT * from choir_president")
    ch = f.fetchall()
    f.execute("SELECT SUM(votes) from choir_president")
    o = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'choir_president'", (o,))
    result.commit()

    if ch[0][1] > ch[1][1]:
        c_ch = ch[0][0]
    elif ch[0][1] == ch[1][1]:
        c_ch = 'A tie'
    else:
        c_ch = ch[1][0]

    f.execute("SELECT * from organizing_sec")
    org = f.fetchall()
    f.execute("SELECT SUM(votes) from organizing_sec")
    q = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'organizing_sec'", (q,))
    result.commit()

    if org[0][1] > org[1][1]:
        c_org = org[0][0]
    elif org[0][1] == org[1][1]:
        c_org = 'A tie'
    else:
        c_org = org[1][0]


    f.execute("SELECT * from prayer_sec")
    pry = f.fetchall()
    f.execute("SELECT SUM(votes) from prayer_sec")
    r = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'prayer_sec'", (r,))
    result.commit()

    if pry[0][1] > pry[1][1]:
        c_pry = pry[0][0]
    elif pry[0][1] == pry[1][1]:
        c_pry = 'A tie'
    else:
        c_pry = pry[1][0]


    f.execute("SELECT * from sch_cord")
    sc = f.fetchall()
    f.execute("SELECT SUM(votes) from sch_cord")
    t = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'sch_cord'", (t,))
    result.commit()

    if sc[0][1] > sc[1][1]:
        c_sc = sc[0][0]
    elif sc[0][1] == sc[1][1]:
        c_sc = 'A tie'
    else:
        c_sc = sc[1][0]

    f.execute("SELECT * from welfare_chair")
    wel = f.fetchall()
    f.execute("SELECT SUM(votes) from welfare_chair")
    w = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'welfare_chair'", (w,))
    result.commit()

    if wel[0][1] > wel[1][1]:
        c_wel = wel[0][0]
    elif wel[0][1] == wel[1][1]:
        c_wel = 'A tie'
    else:
        c_wel = wel[1][0]



     
    f.execute("SELECT * from evang_cord")
    env = f.fetchall()
    f.execute("SELECT SUM(votes) from evang_cord")
    v = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'evang_cord'", (v,))
    result.commit()







    f.execute("SELECT * from ATL_hall")
    atl = f.fetchall()
    f.execute("SELECT SUM(votes) from ATL_hall")
    b = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'ATL_hall'", (b,))
    result.commit()

    if atl[0][1] > atl[1][1]:
        c_atl = atl[0][0]
    elif atl[0][1] == atl[1][1]:
        c_atl = 'A tie'
    else:
        c_atl = atl[1][0]



    f.execute("SELECT * from KNH_hall")
    knh = f.fetchall()
    f.execute("SELECT SUM(votes) from KNH_hall")
    d = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'KNH_hall'", (d,))
    result.commit()

    if knh[0][1] > knh[1][1]:
        c_knh = knh[0][0]
    elif knh[0][1] == knh[1][1]:
        c_knh = 'A tie'
    else:
        c_knh = knh[1][0]

    f.execute("SELECT * from Casford_hall")
    Casford = f.fetchall()
    f.execute("SELECT SUM(votes) from Casford_hall")
    h = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'Casford_hall'", (h,))
    result.commit()

    if Casford[0][1] > Casford[1][1]:
        c_Casford = Casford[0][0]
    elif Casford[0][1] == Casford[1][1]:
        c_Casford = 'A tie'
    else:
        c_Casford = Casford[1][0]

    f.execute("SELECT * from Oguaa_hall")
    Oguaa = f.fetchall()
    f.execute("SELECT SUM(votes) from Oguaa_hall")
    j = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'Oguaa_hall'", (j,))
    result.commit()

    if Oguaa[0][1] > Oguaa[1][1]:
        c_Oguaa = Oguaa[0][0]
    elif Oguaa[0][1] == Oguaa[1][1]:
        c_Oguaa = 'A tie'
    else:
        c_Oguaa = Oguaa[1][0]

    f.execute("SELECT * from SRC_hall")
    src = f.fetchall()
    f.execute("SELECT SUM(votes) from SRC_hall")
    k = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'SRC_hall'", (k,))
    result.commit()

    if src[0][1] > src[1][1]:
        c_src = src[0][0]
    elif src[0][1] == src[1][1]:
        c_src = 'A tie'
    else:
        c_src = src[1][0]

    f.execute("SELECT * from Superannuation")
    sup = f.fetchall()
    f.execute("SELECT SUM(votes) from Superannuation")
    l = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'Superannuation'", (l,))
    result.commit()

    if sup[0][1] > sup[1][1]:
        c_sup = sup[0][0]
    elif sup[0][1] == sup[1][1]:
        c_sup = 'A tie'
    else:
        c_sup = sup[1][0]


    f.execute("SELECT * from Valco_hall")
    valc = f.fetchall()
    f.execute("SELECT SUM(votes) from Valco_hall")
    m = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'Valco_hall'", (m,))
    result.commit()

    if valc[0][1] > valc[1][1]:
        c_valc = valc[0][0]
    elif valc[0][1] == valc[1][1]:
        c_valc = 'A tie'
    else:
        c_valc = valc[1][0]
    


    
    f.execute("SELECT * from Adehye_hall")
    adh = f.fetchall()
    f.execute("SELECT SUM(votes) from Adehye_hall")
    z = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'Adehye_hall'", (z,))
    result.commit()

 









    f.execute("SELECT * from Amamoma")
    ama = f.fetchall()
    f.execute("SELECT SUM(votes) from Amamoma")
    e = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'Amamoma'", (e,))
    result.commit()

    if ama[0][1] > ama[1][1]:
        c_ama = ama[0][0]
    elif ama[0][1] == ama[1][1]:
        c_ama = 'A tie'
    else:
        c_ama = ama[1][0]



    f.execute("SELECT * from Apewosika")
    ape = f.fetchall()
    f.execute("SELECT SUM(votes) from Apewosika")
    g = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'Apewosika'", (g,))
    result.commit()

    if ape[0][1] > ape[1][1]:
        c_ape = ape[0][0]
    elif ape[0][1] == ape[1][1]:
        c_ape = 'A tie'
    else:
        c_ape = ape[1][0]

    f.execute("SELECT * from Kwaprow")
    kwa = f.fetchall()
    f.execute("SELECT SUM(votes) from Kwaprow")
    i = f.fetchone()[0]
    f.execute("UPDATE Total_votes SET votes=? WHERE Position= 'Kwaprow'", (i,))
    result.commit()

    if kwa[0][1] > kwa[1][1]:
        c_kwa = kwa[0][0]
    elif kwa[0][1] == kwa[1][1]:
        c_kwa = 'A tie'
    else:
        c_kwa = kwa[1][0]





    return render_template('results.html',c_pres=c_pres, pres=pres, c_sec=c_sec, sec=sec, s=s,a=a, b=b, atl=atl, c_atl=c_atl, knh=knh, c_knh=c_knh, d=d, ama=ama, e=e,c_ama=c_ama, ape=ape, c_ape=c_ape, g=g, Casford=Casford, c_Casford=c_Casford,h=h, kwa=kwa, c_kwa=c_kwa, i=i,j=j, c_Oguaa=c_Oguaa, Oguaa=Oguaa,k=k, src=src,c_src=c_src, sup=sup,c_sup=c_sup,l=l, valc=valc, c_valc=c_valc, m=m, cs=cs, c_cs=c_cs, n=n, ch=ch, c_ch=c_ch, o=o, org=org, c_org=c_org, q=q, pry=pry,r=r, sc=sc, t=t, adh=adh, z=z, wel=wel, w=w, env=env, v=v)




@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.secret_key = b'haha... its a generated key' # i had an error when i was running the app i guess we can use another secured method like a random number generator or something
    # images = Images(app)
    app.run(debug=True, port=7000)