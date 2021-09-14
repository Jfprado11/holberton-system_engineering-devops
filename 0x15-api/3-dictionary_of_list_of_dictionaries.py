#!/usr/bin/python3
"""gathering the information of an apy"""

import json
import requests

if __name__ == "__main__":

    info = requests.get(
        "https://jsonplaceholder.typicode.com/users/")

    users = info.json()

    datas = {}
    for user in users:
        data = []
        values = {"userId": user["id"]}
        todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos/", params=values)
        todos = todos.json()
        for todo in todos:
            data.append({"username": user["username"], "task": todo["title"],
                        "completed": todo["completed"]})
        datas[user["id"]] = data

    with open("todo_all_employees.json", "w", newline="") as file:
        json.dump(datas, file)
