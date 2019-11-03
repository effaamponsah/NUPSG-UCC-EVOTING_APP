from flask import Flask, request, render_template

def msg():
    user = request.cookies.get('userId')
    return render_template('error.html', user=user)