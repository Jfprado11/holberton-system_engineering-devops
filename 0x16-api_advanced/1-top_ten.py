#!/usr/bin/python3
"""print the title for 10 hot post"""

import requests


def top_ten(subreddit):
    """the ten hottest reddits"""
    params = {"limit": 10}
    headers = {"User-agent": "holbie"}
    data = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit),
        allow_redirects=False,
        params=params, headers=headers)
    if data.status_code == 200:
        data = data.json()
        posts = data["data"]["children"]
        if data["data"]["dist"] == 0:
            print(None)
        else:
            for post in posts:
                print(post["data"]["title"])
    else:
        print(None)
