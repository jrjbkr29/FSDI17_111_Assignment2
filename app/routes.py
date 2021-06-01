#!/usr/bin/env python3
"""HTTP route definitions"""


from flask import request, render_template, make_response, jsonify
from app import app # from the app package import the app variable
from app.database import (
    create,
    scan,
    delete,
    delete_user,
    update_user,
)

@app.route('/')
def user():
    users = scan()
    return render_template('users.html', users=users)


@app.route("/new_user", methods=["POST"])      
def create_user():                          
    user_data = request.form
    new_id = create(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
    )
    return render_template("result.html", result=user_data, new_id=new_id)


@app.route("/users/delete", methods=["POST"])   
def delete_users():
    delete()
    return "<h2>Successfully DELETED ALL users</h2><a class='navbar-brand' href='/'>My App</a>"

@app.route("/user/delete/<int:user_id>", methods=["POST"])   
def delete_usr(user_id):
    user_id = request.form
    id = (user_id.get("id"))
    print(id)
    delete_user(id)
    return "<h2>Successfully DELETED user</h2><a class='navbar-brand' href='/'>My App</a>"

@app.route("/user/update/<id>", methods=["POST"])   
def update_usr(id):
    user_data = request.form
    print(user_data)
    user_update = update_user(
        id,
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
        )
    return "<h2>Successfully Updated user</h2><a class='navbar-brand' href='/'>My App</a>"