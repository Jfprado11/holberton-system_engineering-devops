#!/usr/bin/python3
"""print the title for 10 hot post"""

import requests


def top_ten(subreddit):
    """the ten hottest reddits"""
    params = {"q": subreddit, "sort": "hot", "limit": 10}
    headers = {"User-agent": "holbie"}
    try:
        data = requests.get("https://www.reddit.com/search.json",
                            params=params, headers=headers)
        if data.status_code == 200:
            data = data.json()
            posts = data["data"]["children"]
            if data["dist"] == 0:
                for post in posts:
                    print(post["data"]["title"])
            else:
                print(None)
    except:
        print(None)
