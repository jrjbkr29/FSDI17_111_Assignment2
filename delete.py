#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Helper file to test endpoints manually"""

import requests
from pprint import pprint


def delete():
    url = "http://127.0.0.1:5000/users/delete/"
    test_data = {
        "first_name": "John"
    }
    out = requests.delete(url, json=test_data)
    try:
        pprint(out.json())
    except Exception:
        pprint(out.text)

if __name__ == "__main__":
    print("Delete request:")
    delete()