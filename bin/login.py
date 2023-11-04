from flask import Blueprint, Flask, request, redirect, url_for, flash
from flask import render_template
from flask_login import login_user, logout_user, login_required, current_user
from bin import api
from flask import current_app as app

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_active:
        return redirect(url_for('home_page'))
    if request.method == 'POST':
        input_id = request.form.get("user_id")
        input_password = request.form.get("password")
        user = api.User.get(input_id)
        if user:
            print(api.User.is_admin(user))
            if api.User.is_admin(user):
                return admin_login(user)
            elif user.password == input_password:
                login_user(user, remember=True)
                return redirect(url_for('home_page'))
    return render_template('login.html', user=current_user)

@app.route("/admin_login", methods=['GET', 'POST'])
def admin_login(user):
    login_user(user, remember=True)
    return redirect(url_for('admin_dashboard'))