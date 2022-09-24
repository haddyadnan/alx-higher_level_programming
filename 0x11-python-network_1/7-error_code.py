#!/usr/bin/python3

"""
A Python script that takes in a URL
sends a request to the URL
and displays the body of the response.
"""


if __name__ == "__main__":
    import requests
    from requests.exceptions import HTTPError
    import sys

    url = sys.argv[1]
    try:
        resp = requests.get(url)
        print(resp.text)
    except HTTPError as e:
        if e >= 400:
            print(f"Error Code {e}")
