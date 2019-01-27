
from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
import json, os

from utils.counter import increment

hall=''
c_residence=''

def chapelsteward_view(wing_name2):
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Chapel-Steward']['role']
        name = data['Chapel-Steward']['name']
        img = data['Chapel-Steward']['images']

    if request.method == 'POST':
        vote = request.form['like']
        increment('chapel_steward', vote)
        #print('Voted for', vote)

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