#!/usr/bin/env python3
"""Module init file"""

from flask import Flask
app = Flask(__name__) # dunder variable or magic variable

from app import routes

