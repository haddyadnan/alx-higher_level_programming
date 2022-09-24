#!/usr/bin/python3

"""
A Python script that takes in a URL
sends a request to the URL
and displays the body of the response.
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    resp = requests.get(url)
    try:
        resp.raise_for_status()
        print(resp.text)
    except:
        print(f"Error Code {resp.status_code}")
