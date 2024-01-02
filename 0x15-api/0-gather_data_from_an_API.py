#!/usr/bin/python3
""" script that gets info about an employee """
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    result = requests.get(user)
    jsonn = result.json()

    print('Employee {} is done with tasks'.format(jsonn.get('name')), end='')

    todo = '{}todos?userId={}'.format(url, sys.argv[1])
    result = requests.get(todo)
    tasks = result.json()
    task_l = []

    for task in tasks:
        if task.get('completed') is True:
            task_l.append(task)

    print("({}/{}):".format(len(task_l), len(tasks)))
    for task in task_l:
        print("\t {}".format(task.get('title')))
