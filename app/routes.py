#!/usr/bin/env python3
"""HTTP route definitions"""


from flask import request
from app import app # from the app package import the app variable
from app.database import (
    create,
    scan
)

@app.route("/users", methods=["POST"])      # decorator, building a map of the routes
def create_user():                          # view functions
    user_data = request.json
    new_id = create(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
    )
    return {
        "ok": True,
        "message": "Success",
        "new_id": new_id
      }

@app.route("/users")
def get_all_users():
    users = scan()
    return {
        "ok": True,
        "message": "Success",
        "users": users
    }

@app.route('/user/<name>')
def user(name):
    return "<h1>Hello, %s!</h1>" % name

@app.route('/square/<int:number>')
def square(number):
    return "<h1>%s squared is %s</h1>" % (number, number**(2))

@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s</p>" % user_agent