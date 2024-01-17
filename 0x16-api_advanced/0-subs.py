#!/usr/bin/python3
"""
module that queries the Reddit API and returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    headers = { "User-Agent": "alx-advanced-api/v1.0 by ohgay_ak4" }
    response = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit), headers=headers)
    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
