#!/usr/bin/python3

"""
a Python that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""


if __name__ == "__main__":
    import requests
    import sys

    rq = requests.get(sys.argv[1])
    print(rq.headers["X-Request-Id"])
