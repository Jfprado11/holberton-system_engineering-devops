#!/usr/bin/python3
"""gathering the information of an apy"""

import requests
import sys

if __name__ == "__main__":

    person = sys.argv[1]
    info = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(person))

    user = info.json()
    false_value = {"userId": user["id"], "completed": "false"}
    todos_false = requests.get(
        "https://jsonplaceholder.typicode.com/todos/", params=false_value)

    ready_value = {"userId": user["id"], "completed": "true"}
    todos_ready = requests.get(
        "https://jsonplaceholder.typicode.com/todos/", params=ready_value)

    todos_false = todos_false.json()
    todos_ready = todos_ready.json()
    todos = len(todos_false) + len(todos_ready)

    text = "Employee {} is done with tasks ({}/{}):".format(
        user["name"], len(todos_ready), todos)

    print(text)
    for todo in todos_ready:
        print(" \t{}".format(todo["title"]))
