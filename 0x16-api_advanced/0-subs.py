#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ queries the Reddit API """

    useragent = 'Mozilla/5.0'

    headers = {
        'User-Agent': useragent
    }
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return 0
    d = req.json()
    if 'data' not in d:
        return 0
    if 'subscribers' not in d.get('data'):
        return 0
    return req.json()['data']['subscribers']
