#!/usr/bin/python3
"""
A script that takes repository name and owner name and list 10 commits
(from the recent to the oldest)
"""
import sys
import requests

if __name__ == '__main__':

    repo_name, repo_owner = sys.argv[1:3]
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"

    req = requests.get(url)
    if req.status_code == 200:
        for commit in req.json()[:10]:
            print("{}: {}".format(
                commit.get('sha'),
                commit.get('commit').get('author').get('name')
            ))
