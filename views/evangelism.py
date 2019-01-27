
from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
import json, os
from utils.counter import increment


wing_name=''
wing_name2=''
hall=''
c_residence=''

def evangelism_view(wing):
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Evangelism-Coordinator']['role']
        name = data['Evangelism-Coordinator']['name']
        img = data['Evangelism-Coordinator']['images']

    if request.method == 'POST':
         vote = request.form['like']
         increment('evang_cord', vote)
         #print('Voted for', vote)
         
         ######################
         if wing == 'Organizers':
             return redirect(url_for('cs'))
         elif wing == 'Sch.Cord':
             return redirect(url_for('sc')) 
         elif wing == 'Choir':
             return redirect(url_for('choir')) 
         else:
             return redirect(url_for('hall_name'))


         ######################
         return redirect(url_for('hall_name'))  
    return render_template('evang.html', role= role, name=name, img=img, wing=wing)