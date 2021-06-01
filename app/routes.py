#!/usr/bin/env python3
"""HTTP route definitions"""


from flask import request, render_template, make_response, jsonify
from app import app # from the app package import the app variable
from app.database import (
    create,
    scan,
    delete
)

@app.route("/")
def create_new_user():
    users = scan()
    return render_template("index.html", users=users)

@app.route('/users')
def user():
    users = scan()
    return render_template('users.html', users=users)


@app.route('/result',methods = ['POST', 'GET'])
def new_user():
   if request.method == 'POST':
      result = request.form
      return render_template("users.html",result = result)


@app.route("/new_user", methods=["POST"])      # decorator, building a map of the routes
def create_user():                          # view functions
    user_data = request.form
    new_id = create(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
    )
    return render_template("result.html", result=user_data, new_id=new_id)
    #{
        #"ok": True,
        #"message": "Success",
        #"new_id": new_id
      #}

@app.route("/users/delete", methods=["POST"])      # decorator, building a map of the routes
def delete_user():
    delete()
    return "successfully deleted everything"
    

@app.route("/users2", methods=["GET"])
def get_all_users():
    users = scan()
    return users

#@app.route('/user/<name>')
#def user(name):
 #   return "<h1>Hello, %s!</h1>" % name

@app.route('/square/<int:number>')
def square(number):
    return "<h1>%s squared is %s</h1>" % (number, number**(2))

@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s</p>" % user_agent