#!/usr/bin/python3

"""
a Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    rq = requests.get("https://alx-intranet.hbtn.io/status")
    print(
        f"Body response:\n\t - type: {type(rq.text)}\
        \n\t - content: {rq.content}"
    )
