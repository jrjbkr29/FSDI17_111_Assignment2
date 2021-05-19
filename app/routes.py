#!/usr/bin/env python3
"""HTTP route definitions"""


from flask import request
from app import app # from the app package import the app variable
from app.database import (
    create,
    read,
    update,
    delete,
    scan
)

@app.route("/users", methods=["POST"])      # decorator, building a map of the routes
def create_user():                          # view functions
    user_data = request.jsonnew_id = create(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
    )
    return {
    "ok": True,
     "message": "Success",
      "new_id": new_id
      }