
from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
import json, os
from utils.counter import increment


wing_name=''
wing_name2=''


def residence_view(c_residence):
    if c_residence == 'KNH': 
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['KNH-HALL']['role']
            name = data['KNH-HALL']['name']
            img = data['KNH-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             increment('KNH_hall', vote)
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)
        
    elif c_residence == 'ATL':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['ATL-HALL']['role']
            name = data['ATL-HALL']['name']
            img = data['ATL-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             increment('ATL_hall', vote)
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)
        # return('You wil vote for ATL')

    elif c_residence == 'Oguaa':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Oguaa-HALL']['role']
            name = data['Oguaa-HALL']['name']
            img = data['Oguaa-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             increment('Oguaa_hall', vote)
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'Casford':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Casford-HALL']['role']
            name = data['Casford-HALL']['name']
            img = data['Casford-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             increment('Casford_hall', vote)
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'Valco':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Valco-HALL']['role']
            name = data['Valco-HALL']['name']
            img = data['Valco-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             increment('Valco_hall', vote)
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'SRC':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['SRC-HALL']['role']
            name = data['SRC-HALL']['name']
            img = data['SRC-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             increment('SRC_hall', vote)
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'PSI':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['SRC-HALL']['role']
            name = data['SRC-HALL']['name']
            img = data['SRC-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             increment('SRC_hall', vote)
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'Adehye':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Adehye-HALL']['role']
            name = data['Adehye-HALL']['name']
            img = data['Adehye-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             increment('Adehye_hall', vote)
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'Superannuation':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Superannuation-Hostel']['role']
            name = data['Superannuation-Hostel']['name']
            img = data['Superannuation-Hostel']['images']
        if request.method == 'POST':
             vote = request.form['like']
             increment('Superannuation', vote)
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'Apewosika':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Apewosika']['role']
            name = data['Apewosika']['name']
            img = data['Apewosika']['images']
        if request.method == 'POST':
             vote = request.form['like']
             increment('Apewosika', vote)
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'Kwaprow':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Kwaprow']['role']
            name = data['Kwaprow']['name']
            img = data['Kwaprow']['images']
        if request.method == 'POST':
             vote = request.form['like']
             increment('Kwaprow', vote)
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

        
    elif c_residence == 'Amamoma':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Amamoma']['role']
            name = data['Amamoma']['name']
            img = data['Amamoma']['images']
        if request.method == 'POST':
             vote = request.form['like']
             increment('Amamoma', vote)
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'Ayensu':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Amamoma']['role']
            name = data['Amamoma']['name']
            img = data['Amamoma']['images']
        if request.method == 'POST':
             vote = request.form['like']
             increment('Amamoma', vote)
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    else:
        return redirect(url_for('done'))