from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response
from db import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json, os
from error import msg
from time import sleep

import sqlite3 as sql

wing_name=''
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
    STUDENTS_ID = str(request.form['std_id'])

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
        sleep(1)
        c.execute("SELECT hall_of_affiliation from students WHERE index_no=:k", {"k": STUDENTS_ID})
        y = c.fetchone()
        w = y[0]
        global hall
        hall = w
        sleep(1)
        c.execute("SELECT current_residence from students WHERE index_no=:k", {"k": STUDENTS_ID})
        y = c.fetchone()
        w = y[0]
        global c_residence
        c_residence = w

        #####################################
        if new_stamp:
            print('Has voted as ', new_stamp)
            return redirect(url_for('error'))
        else:
            print("Wing name",wing_name)
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
        if not request.form['name'] or not request.form['std_id']:
            print('Massa fill in the forms')
        else:
            data = Students(
                        request.form['name'],
                        request.form['res'],
                        request.form['std_id'],
                        request.form['hall_of_affiliation'],
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
         v.execute("UPDATE  welfare_chair SET votes =votes+?  WHERE name= ?", (1,vote,))
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
         else:
             return redirect(url_for('hall_name'))  
            #  return redirect(url_for('welfare')) 
             
    return render_template('p_sec.html', role= role, name=name, img=img)

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
         return redirect(url_for('hall_name'))  
    return render_template('sc.html', role= role, name=name, img=img)


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
         return redirect(url_for('hall_name'))  
    return render_template('evang.html', role= role, name=name, img=img)


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
        
        return render_template('hall.html',role=role, name=name, img=img)
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
        
        return render_template('hall.html',role=role, name=name, img=img)
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
        
        return render_template('hall.html',role=role, name=name, img=img)
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
        
        return render_template('hall.html',role=role, name=name, img=img)
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
        
        return render_template('hall.html',role=role, name=name, img=img)
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
        
        return render_template('hall.html',role=role, name=name, img=img)

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
        
        return render_template('hall.html',role=role, name=name, img=img)
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
        
        return render_template('hall.html',role=role, name=name, img=img)
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
    # print(ret)
    ################################################

    # try to loop through for code optimization
    # name1 = ret[0][0]
    # votes1 = ret[0][1]
    # name2 = ret[1][0]
    # votes2 = ret[1][1]
    # optimization successfully done in template :)
    # it wasnt done the same day thi. just in case i happen to look through
    # these codes some time to come

    ##############################################
    if pres[0][1] > pres[1][1]:
        c_pres = pres[0][0]
    elif pres[0][1] == pres[1][1]:
        c_pres = 'A tie'
    else:
        c_pres = pres[1][0]

    f.execute("SELECT * from secretary")
    sec = f.fetchall()
    if sec[0][1] > sec[1][1]:
        c_sec = sec[0][0]
    elif sec[0][1] == sec[1][1]:
        c_sec = 'A tie'
    else:
        c_sec = sec[1][0]
    
    return render_template('result.html',c_pres=c_pres, pres=pres, c_sec=c_sec, sec=sec)





@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.secret_key = b'haha... its a generated key' # i had an error when i was running the app i guess we can use another secured method like a random number generator or something
    # images = Images(app)
    app.run(debug=True, port=8000)