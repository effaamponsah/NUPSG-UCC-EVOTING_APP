from flask import render_template, request

from utils.adminqueries import addStudent

def admin_view():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['std_id']:
            pass
        else:

            addStudent(request.form['name'],
            str(request.form['std_id']).upper(),
            request.form['hall_of_affiliation'],
            request.form['res'],
            request.form['wing'],
            request.form['wing2'],
            )
            return  '''
                <h2>Data Successfully added</h2>
                <a href='/admin'>Add again</a>
            '''
    return render_template('/admin.html')