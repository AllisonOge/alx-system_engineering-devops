#!/usr/bin/python3
"""
Task: Count it!

Write a recursive function that queries the Reddit API,
pases the title of all hot articles, and prints a sorted
count of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).

Prototype: def count_words(subreddit, word_list)
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Returns a sorted count of given keywords
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'CustomUserAgent/1.0'
    }
    params = {
        'limit': 100,
        'after': after
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get('data').get('children')

    for i in range(len(data)):
        title = data[i].get('data').get('title')
        title_words = title.split()
        for word in word_list:
            word = word.lower()
            if word in title_words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    after = response.json().get('data').get('after')
    if after is None:
        if not word_count:
            return None
        for word in sorted(word_count.keys()):
            print('{}: {}'.format(word, word_count[word]))
        return

    return count_words(subreddit, word_list, after, word_count)
