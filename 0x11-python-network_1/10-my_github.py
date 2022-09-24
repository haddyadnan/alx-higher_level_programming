#!/usr/bin/python3

"""
A Python script that takes your GitHub credentials (username and password)
uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    import sys

    user = sys.argv[1]
    token = sys.argv[2]

    resp = requests.get("https://api.github.com/user", auth=(user, token)).json()
    try:
        print(f"{resp['id']}")
    except Exception:
        print("None")
