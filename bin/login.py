from flask import Blueprint, Flask, request, redirect, url_for, flash
from flask import render_template
from flask_login import login_user, logout_user, login_required, current_user
from bin import api
from flask import current_app as app

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_active:
        return redirect(url_for('home_page'))
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        email = request.form.get('email')
        if password != confirm_password:
            flash('Password doesn\'t match!')
            return redirect(url_for('register'))
        else:
            try:
                api.User.add(user_name=user_name, password=password, email=email)
                flash(f'Welcome, {user_name}!')
                return redirect(url_for('login'))
            except:
                flash(f'User already exists!')
                return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_active:
    #     return redirect(url_for('home_page'))

    if request.method == 'POST':
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        user = api.User.get(user_name)
        if user:
            print('current user:',user)
            if api.User.is_admin(user):
                flash('Redirecting to admin login...')
                return admin_login(user)
            elif user.password == password:
                print('user in login:',user)
                print(user.user_name, 'logging in, is active?', user.is_active)
                login_user(user, remember=True)
                flash('Logged in successfully!')
                return redirect(url_for('home_page'))
        else:
            flash('User doesn\'t exist!')
            return redirect(url_for('register'))
    return render_template('login.html', user=current_user)

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login(user):
    login_user(user, remember=True)
    return redirect(url_for('admin_dashboard'))