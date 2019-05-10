#!/usr/env python3


import requests
import sys
import datetime
import json


def get_repo(username):
    result = []
    user_url = "https://api.github.com/users/" + username + "/repos"
    resp = requests.get(user_url)
    data = json.loads(resp.text)
    print("List of repository(s) in", username)

    for item in data:
        repo_name = item["name"]

        if not item["html_url"]:
            repo_url = user_url + repo_name
        else:
            repo_url = item["html_url"]

        repo_create_date = datetime.datetime.strptime(
            item["created_at"], "%Y-%m-%dT%H:%M:%SZ"
            )

        result.append((repo_name, repo_url, repo_create_date))
        print("{} {} {}".format(
            repo_name, repo_url, repo_create_date.strftime("%d %b %Y"))
            )
    print("Total repository(s):")
    return len(result)


def main():
    username = sys.argv[1]

    print(get_repo(username))


if __name__ == "__main__":
    main()
