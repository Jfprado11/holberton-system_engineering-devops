#!/usr/bin/python3
"""requesting an api of reddit """

import requests


def number_of_subscribers(subreddit):
    """returns the numbers of subs in reddit"""
    headers = {"User-agent": "holbie"}
    try:
        r = requests.get(
            "https://www.reddit.com/r/{}/about/.json".format(
                subreddit), headers=headers)
        data = r.json()
        return(data["data"]["subscribers"])
    except:
        return(0)
