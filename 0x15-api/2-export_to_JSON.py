#!/usr/bin/python3
"""gathering the information of an apy"""

import json
import requests
import sys

if __name__ == "__main__":

    person = sys.argv[1]
    info = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(person))

    user = info.json()
    values = {"userId": user["id"]}
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/", params=values)

    todos = todos.json()

    data = []
    for todo in todos:
        data.append([{"task": todo["title"],
                     "completed": todo["completed"],
                      "username": user["username"]}])
    datas = {user["id"]: data}

    with open("{}.json".format(user["id"]), "w", newline="") as file:
        json.dump(datas, file)
