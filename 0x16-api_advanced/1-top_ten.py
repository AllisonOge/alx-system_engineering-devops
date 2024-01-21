#!/usr/bin/python3
"""module that queries Reddit API and prints the titles of the
first 10 host posts listed for a given subreddit"""
import requests



def top_ten(subreddit):
    """prints the titles of the first top 10 hot posts"""
    headers = {"User-Agent": "0x16-advanced-api/1.0 by /u/ohgay_ak4"}
    res = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
		       headers=headers)
    print(res.status_code)
    data = res.json() if res.status_code == 200 else {}
    for post in data.get("data", {}).get("children", []):
        print(post["data"]["title"])
