from flask import Flask, flash, redirect, request, url_for, views
from flask import render_template
from flask import current_app as app
from flask_login import current_user, login_required, login_user
from bin import api

@app.route("/home_page", methods=["GET", "POST"])
@login_required
def home_page():
    return render_template("home_page.html", user=current_user)

@app.route('/')
def home():
    return redirect('/login')

