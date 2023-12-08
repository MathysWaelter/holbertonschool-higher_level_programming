#!/usr/bin/python3

import urllib.request

"""
Python script that fetches https://intranet.hbtn.io/status
"""

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print(type(html))
