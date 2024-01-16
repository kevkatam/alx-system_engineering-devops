#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ queries the reddit api """

    useragent = 'Mozilla/5.0'

    headers = {
        'User-Agenti': useragent
    }
    params = {
        'limit': 10
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    req = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if req.status_code != 200:
        print(None)
        return
    d = req.json
    h_posts = d['data']['children']
    if len(h_posts) == 0:
        print(None)
    else:
        for title in h_posts:
            print(post['data']['title'])
