
from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
import json, os
import sqlite3 as sql


wing_name=''
wing_name2=''


def residence_view(c_residence):
    pres_vt = sql.connect('polls.db')
    v = pres_vt.cursor()
    if c_residence == 'KNH': 
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['KNH-HALL']['role']
            name = data['KNH-HALL']['name']
            img = data['KNH-HALL']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE KNH_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
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
             v.execute("UPDATE ATL_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
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
             v.execute("UPDATE Oguaa_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
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
             v.execute("UPDATE Casford_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
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
             v.execute("UPDATE Valco_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
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
             v.execute("UPDATE SRC_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
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
             v.execute("UPDATE SRC_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
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
             v.execute("UPDATE Adehye_hall SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    elif c_residence == 'SUPERANNUATION':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Superannuation-Hostel']['role']
            name = data['Superannuation-Hostel']['name']
            img = data['Superannuation-Hostel']['images']
        if request.method == 'POST':
             vote = request.form['like']
             v.execute("UPDATE Superannuation SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
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
             v.execute("UPDATE Apewosika SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
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
             v.execute("UPDATE Kwaprow SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
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
             v.execute("UPDATE Amamoma SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
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
             v.execute("UPDATE Amamoma SET votes =votes+?  WHERE name= ?", (1,vote,))
             pres_vt.commit()
             #print('Voted for', vote)
             return redirect(url_for('done'))
        return render_template('c_res.html',role=role, name=name, img=img)

    else:
        return redirect(url_for('done'))