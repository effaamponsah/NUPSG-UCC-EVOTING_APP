
from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
import json, os
import sqlite3 as sql


wing_name=''
wing_name2=''
hall=''
c_residence=''


def president_view():
    pres_vt = sql.connect('polls.db')
    v = pres_vt.cursor()
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['President']['role']
        name = data['President']['name']
        img = data['President']['images']

    if request.method == 'POST':
        vote = request.form['like']   #do a check on the when the user selects none
        if vote == '':
            #print('User never choose anyone to vote for')
            pass
            
        v.execute("UPDATE president SET votes =votes+?  WHERE name= ?", (1,vote,))
        pres_vt.commit()
        #print('Voted for', vote)
        return redirect(url_for('sec'))   #this is where the logic for solving the hall and wings problem will be about. Here we can use a switch case or a simple if-else
    return render_template('pres.html', role=role, img=img, name=name)

    # return render_template(url_for('logout'))
