#!/usr/bin/python3
"""gathering the information of an apy"""

import csv
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

    with open("{}.csv".format(user["id"]), "w", newline="") as file:
        writer = csv.writer(file)

        for todo in todos:
            data = [user["id"], user["username"],
                    todo["completed"], todo["title"]]
            writer.writerow(data)
