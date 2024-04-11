#!/usr/bin/python3

"""
Task 2: Recurse it!

Write a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the given
subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Prototype: def recurse(subreddit, hot_list=[])
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Returns a list containing the titles of all hot articles
    for a given subreddit
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'CustomUserAgent/1.0'
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json().get('data').get('children')

    for i in range(len(data)):
        hot_list.append(data[i].get('data').get('title'))

    after = response.json().get('data').get('after')
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list)
