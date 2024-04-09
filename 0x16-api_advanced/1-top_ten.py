#!/usr/bin/python3

"""
Task 1: Top Ten

Write a function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit.

Prototype: def top_ten(subreddit)
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts
    listed for a given subreddit
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        # 'User-Agent': 'Python:alx-api-advanced:v0.1 (by /u/ohgay_ak4)'
        'User-Agent': 'CustomUserAgent/1.0'
    }
    response = requests.get(url, headers=headers)

    # print(response.status_code, response.reason)
    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data').get('children')

    for i in range(10):
        print(data[i].get('data').get('title'))
