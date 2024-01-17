#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""
import re
import requests


def title(dic, h_posts):
    """ function that adds title to a list """
    if len(h_posts) == 0:
        return

    title = (h_posts[0]['data']['title']).split()
    for word in title:
        for key in dic.keys():
            comp = re.compile("^{}$".format(key), re.I)
            if comp.findall(word):
                dic[key] += 1
    h_posts.pop(0)
    title(dic, h_posts)


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


def count_words(subreddit, word_list):
    """ Function to Initialize and Print Word Counts """
    dic = {}
    for word in word_list:
        dic[word] = 0

    recurse(subreddit, dic)
    sort = sorted(dic.items(), key=lambda kv: kv[1])
    sort.reverse()

    if len(sort) != 0:
        for item in sort:
            if item[1] != 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
