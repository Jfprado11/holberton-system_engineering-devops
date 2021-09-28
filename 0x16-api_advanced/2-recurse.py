#!/usr/bin/python
"""return the hot posts for subredist"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """recursive append the list"""
    params = {"limit": 1, "after": after}
    headers = {"User-agent": "holbie"}
    data = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit), allow_redirects=False,
        params=params, headers=headers)
    if data.status_code == 200:
        data = data.json()
        posts = data["data"]["children"]
        after = data["data"]["after"]
        try:
            hot_list.append(posts[0]["data"]["title"])
            count += 1
            recurse(subreddit, hot_list, after, count)
        except:
            return (hot_list)
    else:
        return(None)