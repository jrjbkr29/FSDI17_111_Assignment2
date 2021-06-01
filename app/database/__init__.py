#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Database operations"""

from flask import g     # context; g is basically a global context
import sqlite3          # python package that allows interaction with sqlite3

DATABASE="user_db"      # creating global variable that defines database file name


def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def output_formatter(results: tuple):
    out = []
    for result in results:
        res_dict = {}
        res_dict["id"] = results[0]
        res_dict["first_name"] = results[1]
        res_dict["last_name"] = results[2]
        res_dict["hobbies"] = results[3]
        out.append(res_dict)
    return out

def scan():
    cursor = get_db().execute("SELECT * FROM user", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def create(first_name, last_name, hobbies):
    value_tuple = (first_name, last_name, hobbies)
    query = """
            INSERT into user (
                first_name,
                last_name,
                hobbies
            ) VALUES (?, ?, ?)
        """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    return last_row_id

def delete():
    sql = 'DELETE FROM tasks'
    cursor = get_db()
    cursor.execute(sql)
    cursor.commit()