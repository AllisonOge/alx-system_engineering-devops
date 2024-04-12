#!/usr/bin/python3
"""
Task 2: Export to JSON

Expand the `0-get_data_from_an_API.py` script to export
the data to a JSON file.

Requirements:
- Records all tasks that are owned by this employee
- Format must be: { "USER_ID": [ {"task": "TASK_TITLE",
                                   "completed": TASK_COMPLETED_STATUS,
                                   "username": "USERNAME"}},
                                 { "task": "TASK_TITLE",
                                   "completed": TASK_COMPLETED_STATUS,
                                   "username": "USERNAME"}},
                                   ...
                                ]}
- File name must be: USER_ID.json
"""

import json
import requests
import sys


def main(employeeId):
    """
    Export the employee TODO list progress
    to a JSON file
    """
    url = "https://jsonplaceholder.typicode.com/users/{}"\
          .format(employeeId)
    response = requests.get(url)
    employee = response.json()
    name = employee.get("name")
    url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
          .format(employeeId)
    response = requests.get(url)
    todos = response.json()
    filename = "{}.json".format(employeeId)
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump({employeeId: [{"task": task.get("title"),
                                 "completed": task.get("completed"),
                                 "username": name} for task in todos]}, file)


if __name__ == "__main__":
    main(sys.argv[1])
