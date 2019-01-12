from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
import json, os
import sqlite3 as sql

wing_name=''
wing_name2=''
hall=''
c_residence=''


def organizers_view():
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
         #print('Voted for', vote)
         return redirect(url_for('welfare'))  
    return render_template('org.html', role= role, name=name, img=img)