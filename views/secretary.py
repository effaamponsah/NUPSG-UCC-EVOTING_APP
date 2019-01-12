from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
import json, os
import sqlite3 as sql


wing_name=''
wing_name2=''
hall=''
c_residence=''


def secretary_view():
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
         #print('Voted for', vote)
         return redirect(url_for('org'))  
    return render_template('sec.html', role= role, name=name, img=img)