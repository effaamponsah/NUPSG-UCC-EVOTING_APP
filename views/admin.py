from flask import Flask, render_template, session, request, flash, url_for, get_flashed_messages, redirect, make_response, g
from db import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json, os



engine = create_engine('sqlite:///tut.db', echo=False)

Session = sessionmaker(bind=engine)
dennis = Session()

def admin_view():
    if request.method == 'POST':
        ID = str(request.form['std_id']).upper()
        if not request.form['name'] or not request.form['std_id']:
            #print('Massa fill in the forms')
            pass
        else:
            data = Students(
                        request.form['name'],
                        request.form['res'],
                        ID,
                        request.form['hall_of_affiliation'],
                        request.form['wing'],
                        request.form['wing2'],
                    )
            dennis.add(data)
            dennis.commit()
            #print('Data Successfully added')
            return  '''
                <h2>Data Successfully added</h2>
                <a href='/admin'>Go back</a>
            '''
    return render_template('/admin.html')