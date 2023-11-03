from flask import Blueprint, Flask, request, redirect, url_for, flash
from flask import render_template
from flask_login import login_user, logout_user, login_required, current_user
from bin import api
from flask import current_app as app

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        input_id = request.form.get("user_id")
        input_password = request.form.get("password")
        user = api.User.get(input_id)
        print(user)
        if user:
            if user.password == input_password:
                print('yay')
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('home_page'))
            else:
                print('aw')
                flash("Password is incorrect!", category='error')
        else:
            flash('User does not exist!', category='error')
    return render_template('login.html', user=current_user)