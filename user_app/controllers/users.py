from flask import Flask, render_template, request, redirect
from user_app import app
from user_app.models.user import User


@app.route("/")
def indes():
    return render_template("index.html")


@app.post("/creates/user")
def create_user():
    user_id = User.create(request.form)
    return redirect("/users")


@app.route("/users")
def display_user():
    users = User.get_all()
    return render_template("all_users.html", users=users)


@app.route("/users/<int:user_id>")
def get_one(user_id):
    user = User.get_one(user_id)
    return render_template("one_user.html", user=user)
