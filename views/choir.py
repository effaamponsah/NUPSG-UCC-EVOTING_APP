
from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
import json, os
import sqlite3 as sql


wing_name=''
wing_name2=''
hall=''
c_residence=''


def choir_view():
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
         #print('Voted for', vote)
         
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