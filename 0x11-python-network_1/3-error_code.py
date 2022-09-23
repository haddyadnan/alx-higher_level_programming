#!/usr/bin/python3

"""
This that takes in a URL,
sends a request to the UR
Land displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    from urllib import response
    import urllib.request
    from urllib.error import HTTPError
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print(f"Error code: {e.code}")
    else:
        response.read()
