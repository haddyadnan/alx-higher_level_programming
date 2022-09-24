#!/usr/bin/python3

"""
A Python script that takes in a letter
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    data = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    try:
        resp = requests.post(url, data=data).json()
        if len(resp) == 0:
            print("No result")
        else:
            print(f"[{resp['name']}] {resp['id']}")
    except Exception:
        print("Not a valid JSON")
