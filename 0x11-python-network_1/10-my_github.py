#!/usr/bin/python3
"""
A script takes GitHub credentials (username and password)
and uses the GitHub API to display user id
"""
import sys
import requests

if __name__ == '__main__':
    username, password = sys.argv[1:3]
    url = f"https://api.github.com/user"
    res = requests.get(url, auth=(username, password))
    if res.status_code == 200:
        json_response = res.json()
        print("{id}".format(**json_response))
    else:
        print(None)
