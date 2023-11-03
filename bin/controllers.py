from flask import Flask, request
from flask import render_template
from flask import current_app as app
from bin import api

@app.route("/<user_id>", methods=["GET", "POST"])
def articles(user_id):
    user = api.User.get(user_id)    
    return render_template("home_page.html", user=user)
