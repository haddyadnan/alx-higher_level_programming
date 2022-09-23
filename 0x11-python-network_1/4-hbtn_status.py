#!/usr/bin/python3

"""
a Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests

rq = requests.get("https://alx-intranet.hbtn.io/status")
print(f"Body response:\n\t - type: {type(rq.text)}\n\t - content: {rq.content}")
