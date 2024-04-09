#!/usr/bin/python3

"""
Task 0: How many subs?

Write a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid subreddit
is given, the function should return 0.

Prototype: def number_of_subscribers(subreddit)
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        # 'User-Agent': 'Python:alx-api-advanced:v0.1 (by /u/ohgay_ak4)'
        'User-Agent': 'CustomUserAgent/1.0'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers', 0)
