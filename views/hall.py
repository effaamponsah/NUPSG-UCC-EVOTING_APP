
from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
import json, os
from utils.counter import increment


wing_name=''
wing_name2=''



def hall_view(hall, c_residence):
    #print('Hall', hall)
    #print('Current', c_residence)
    # if hall and c_residence == 'ATL':
    if hall == 'ATL':  
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['ATL-HALL']['role']
            name = data['ATL-HALL']['name']
            img = data['ATL-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            increment('ATL_hall', vote)
            #print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)
    elif hall == 'KNH':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['KNH-HALL']['role']
            name = data['KNH-HALL']['name']
            img = data['KNH-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            increment('KNH_hall', vote)
            #print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)
    elif hall == 'Valco':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Valco-HALL']['role']
            name = data['Valco-HALL']['name']
            img = data['Valco-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            increment('Valco_hall', vote)
            #print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)
    elif hall == 'Oguaa':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Oguaa-HALL']['role']
            name = data['Oguaa-HALL']['name']
            img = data['Oguaa-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            increment('Oguaa_hall', vote)
            #print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)
    elif hall == 'Casford':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Casford-HALL']['role']
            name = data['Casford-HALL']['name']
            img = data['Casford-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            increment('Casford_hall', vote)
            #print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)
    elif hall == 'SRC':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['SRC-HALL']['role']
            name = data['SRC-HALL']['name']
            img = data['SRC-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            #print('Voted for', vote)
            increment('SRC_hall', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)

    elif hall == 'PSI':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['SRC-HALL']['role']
            name = data['SRC-HALL']['name']
            img = data['SRC-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            increment('SRC_hall', vote)
            #print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)

    elif hall == 'Adehye':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Adehye-HALL']['role']
            name = data['Adehye-HALL']['name']
            img = data['Adehye-HALL']['images']
        if request.method == 'POST':
            vote = request.form['like']
            increment('Adehye_hall', vote)
            ##print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)

    elif hall == 'Superannuation':
        with open(os.path.join('./seed/data.json')) as file:
            data = json.load(file)
            role = data['Superannuation-Hostel']['role']
            name = data['Superannuation-Hostel']['name']
            img = data['Superannuation-Hostel']['images']
        if request.method == 'POST':
            vote = request.form['like']
            increment('Superannuation', vote)
            #print('Voted for', vote)
            if hall == c_residence:
                return redirect(url_for('done'))
            else:
                return redirect(url_for('res_'))
        
        return render_template('hall.html',role=role, name=name, img=img, hall=hall, c_residence=c_residence)
    else:
        return redirect(url_for('done'))