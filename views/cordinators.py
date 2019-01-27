
from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
import json, os
from utils.counter import increment


def cordinators_view(wing_name2):
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Schools Coordinator']['role']
        name = data['Schools Coordinator']['name']
        img = data['Schools Coordinator']['images']

    if request.method == 'POST':
         vote = request.form['like']
         increment('sch_cord', vote)
         #print('Voted for', vote)
         
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