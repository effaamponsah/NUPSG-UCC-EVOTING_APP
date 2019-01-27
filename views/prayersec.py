
from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
import json, os
from utils.counter import increment


hall=''
c_residence=''

def prayersec_view(wing_name):
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Prayer-Secretary']['role']
        name = data['Prayer-Secretary']['name']
        img = data['Prayer-Secretary']['images']

    if request.method == 'POST':
         vote = request.form['like']
         increment('prayer_sec', vote)
         #print('Voted for', vote)

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