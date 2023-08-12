from flask import Flask, render_template, request, redirect
from user_app import app
from user_app.models.user import User


@app.route("/")
def index():
    return render_template("index.html")


@app.post("/creates/user")
def create_user():
    user_id = User.create(request.form)
    return redirect(f"/users/{user_id}")


@app.route("/users")
def display_users():
    users = User.get_all()
    return render_template("all_users.html", users=users)


@app.route("/users/<int:user_id>")
def get_one(user_id):
    user = User.get_one(user_id)
    return render_template("one_user.html", user=user)


@app.route('/users/<int:user_id>/edit')
def display_edit_form(user_id):
    user = User.get_one(user_id)
    return render_template('edit.html', user=user)

@app.post('/users/<int:user_id>/update')
def update_edit_form(user_id):
    User.update(request.form)
    return redirect(f'/users/{user_id}')


@app.post('/users/<int:user_id>/delete')
def delete_user(user_id):
    User.delete(user_id)
    return redirect('/users')