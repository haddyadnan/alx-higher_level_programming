#!/usr/bin/python3

"""
This script script that takes in a URL and an email
sends a POST request to the passed URL
with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
values = {"email": sys.argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode("utf-8")
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    print(response.read().decode("utf-8"))
