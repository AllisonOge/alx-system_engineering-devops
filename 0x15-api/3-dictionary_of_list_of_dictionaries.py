#!/usr/bin/python3
"""
Task 3: Dictionary of list of dictionaries

Expand the `0-get_data_from_an_API.py` script to export
the data to a JSON file.

Requirements:
- Records all tasks from all employees
- Format must be: { "USER_ID": [ {"task": "TASK_TITLE",
                                   "completed": TASK_COMPLETED_STATUS,
                                   "username": "USERNAME"}},
                                 { "task": "TASK_TITLE",
                                   "completed": TASK_COMPLETED_STATUS,
                                   "username": "USERNAME"}},
                                   ...
                                ]}
- File name must be: todo_all_employees.json
"""

import json
import requests


def main():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    employees = response.json()
    todos = {}
    for employee in employees:
        employeeId = employee.get("id")
        name = employee.get("name")
        url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
              .format(employeeId)
        response = requests.get(url)
        tasks = response.json()
        todos[employeeId] = [{"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": name} for task in tasks]
    filename = "todo_all_employees.json"
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(todos, file)


if __name__ == "__main__":
    main()
