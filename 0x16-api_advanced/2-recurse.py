#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""
import requests


def title(hot_list, h_posts):
    """ function that adds title to a list """
    if len(h_posts) == 0:
        return

    hot_list.append(h_posts[0]['data']['title'])
    h_posts.pop(0)
    title(hot_list, h_posts)


def recurse(subreddit, hot_list=[], after=None):
    """queries the Reddit API """
    useragent = 'Mozilla/5.0'

    headers = {
        'User-Agent': useragent
    }
    params = {
        'after': after
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if req.status_code != 200:
        return None
    d = res.json()
    h_posts = d['data']['children']
    title(hot_list, h_posts)
    after = d['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
