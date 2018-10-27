from flask import Flask, request, render_template

def man():
    user = request.cookies.get('userId')
    return render_template('error.html', user=user)