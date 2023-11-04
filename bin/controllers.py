from flask import redirect
from flask import render_template
from flask import current_app as app
from flask_login import current_user, login_required,  logout_user

@app.route('/')
def home():
    return redirect('/login')

@app.route("/home_page")
# @login_required
def home_page():
    print(current_user)
    return render_template('home_page.html', user=current_user)

@app.route("/admin_dashboard")
@login_required
def admin_dashboard():
    return render_template('home_page.html', user=current_user)

@app.route("/logout")
@login_required
def log_out():
    logout_user()
    return redirect('/login')
