
from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
import json, os
import sqlite3 as sql




def welfare_views():
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
         #print('Voted for', vote)
         return redirect(url_for('p_sec'))  
    return render_template('welfare.html', role= role, name=name, img=img)