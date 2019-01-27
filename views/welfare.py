
from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
import json, os
from utils.counter import increment



def welfare_views():
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Welfare-Chairperson']['role']
        name = data['Welfare-Chairperson']['name']
        img = data['Welfare-Chairperson']['images']

    if request.method == 'POST':
         vote = request.form['like']
         increment('welfare_chair', vote)
         #print('Voted for', vote)
         return redirect(url_for('p_sec'))  
    return render_template('welfare.html', role= role, name=name, img=img)