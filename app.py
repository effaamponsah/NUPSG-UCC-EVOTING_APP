from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
import json, os
from error import msg
from views.choir import choir_view
from views.chapelsteward import chapelsteward_view
from views.evangelism import evangelism_view
from views.hall import hall_view
from views.residence import residence_view
from views.cordinators import cordinators_view
from views.prayersec import prayersec_view
from views.welfare import welfare_views
from views.admin import admin_view
from views.organizers import organizers_view
from views.secretary import secretary_view
from utils.studentqueries import studentLogin
from utils.counter import increment, viewResults

wing_name=''
wing_name2=''
hall=''
c_residence=''

app = Flask(__name__)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for('vote'))


@app.route('/login', methods=['POST'])
def login():
    has_voted = False
    STUDENTS_ID = str(request.form['std_id']).upper()
    result = studentLogin(STUDENTS_ID)
    if result:  
        session['logged_in'] = True
        has_voted = True
        new_stamp = request.cookies.get(STUDENTS_ID)

        #####################################
    
        global wing_name
        wing_name = result['wing']

        global hall
        hall = result['hall_of_affiliation']

        global c_residence
        c_residence = result['current_residence']

        global wing_name2
        wing_name2 = result['wing2']

        #####################################
        if new_stamp:
            return redirect(url_for('error'))

    else:
        flash('Index number not found in records. Try again or register')

    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('userId', STUDENTS_ID)


    if has_voted:
        new_stamp = "Should Be Kept Secret"
        resp.set_cookie(STUDENTS_ID, new_stamp)
    return resp


@app.route('/admin', methods=['GET','POST'])  #i thought it would be POST only but when you are trying in the browser, you are getting :)
def admin():
    return admin_view()

       

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return index()


@app.route('/pres', methods=['GET', 'POST'])
def vote():
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['President']['role']
        name = data['President']['name']
        img = data['President']['images']

    if request.method == 'POST':
        increment('president', request.form['like']) 
        return redirect(url_for('sec')) 
    return render_template('pres.html', role=role, img=img, name=name)

@app.route('/sec', methods=['GET', 'POST'])
def sec():  
    return secretary_view()


@app.route('/org', methods=['GET', 'POST'])
def org():
    return organizers_view()


@app.route('/welfare', methods=['GET', 'POST'])
def welfare():
    return welfare_views()


@app.route('/p_sec', methods=['GET', 'POST'])
def p_sec():
    return prayersec_view(wing_name)

@app.route('/cs', methods=['GET', 'POST'])
def cs():
   return chapelsteward_view(wing_name2)


@app.route('/sc', methods=['GET', 'POST'])
def sc():
    return cordinators_view(wing_name2)
    


@app.route('/evang', methods=['GET', 'POST'])
def evang():
    return evangelism_view(wing_name2)
    


@app.route('/choir', methods=['GET', 'POST'])
def choir():
    global wing_name2
    return choir_view(wing_name2)


@app.route('/hall', methods=['GET', 'POST'])
def hall_name():
    return hall_view(hall, c_residence)
    
    

@app.route('/res', methods=['GET', 'POST'])
def res_():
    return residence_view(c_residence)
    

@app.route('/done')
def done():
    return render_template('done.html')


@app.route('/error')
def error():
    return msg()



@app.route('/results')
def result():
    president = viewResults('president')
    secretary = viewResults('secretary')
    adehye = viewResults('adehye_hall')
    amamoma = viewResults('amamoma')
    prayersec = viewResults('prayer_sec')
    cs = viewResults('chapel_steward')
    choir = viewResults('choir_president')
    env = viewResults('evang_cord')
    org = viewResults('organizing_sec')
    sc = viewResults('sch_cord')
    wel = viewResults('welfare_chair')
    ape =viewResults('apewosika')
    kwa = viewResults('kwaprow')
    valc= viewResults('valco_hall')
    sup =viewResults('superannuation')
    src =viewResults('src_hall')
    oguaa =viewResults('oguaa_hall')
    casford = viewResults('casford_hall')
    knh= viewResults('knh_hall')
    atl = viewResults('atl_hall')

    return render_template('results.html',  president=president,secretary=secretary,adehye=adehye,amamoma=amamoma, prayersec=prayersec,cs=cs,choir=choir,env=env,org=org,sc=sc,wel=wel,ape=ape, kwa=kwa,valc=valc,sup=sup,src=src,oguaa=oguaa,casford=casford, knh=knh,atl=atl)




@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.secret_key = b'haha... its a generated key'
    app.run(debug=True)