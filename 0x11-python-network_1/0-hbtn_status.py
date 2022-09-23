#!/usr/bin/python3

"""
This script script fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        ht = response.read()
        print("Body response:")
        print(f"\t - type: {type(ht)}")
        print(f"\t - content: {ht}")
        print(f"\t - utf8 content: {ht.decode('utf-8')}")
