from flask import Flask, render_template, request
import os, json

def data():
    with open(os.path.join('./seed/data.json')) as file:
        data = json.load(file)
        role = data['Organizing-Secretary']['role']
        name = data['Organizing-Secretary']['name']
        img = data['Organizing-Secretary']['images']

    if request.method == 'POST':
         vote = request.form['like']
         print('Voted for', vote)
    return render_template('vote3.html', role= role, name=name, img=img)


