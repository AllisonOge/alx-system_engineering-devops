#!/usr/bin/python3
"""
Task 0: Gather data from an API

Write a Python script that, using this [REST API]
(https://intranet.alxswe.com/rltoken/7cr7aLYdaWAZWBKrBKS12A),
for a given employee ID, returns information about his/her TODO list progress.

Requirements:
- You must use urllib or requests module
- The script must accept an integer as a parameter, which is the employee ID
- The script must display on the standard output the employee
TODO list progress in this exact format:
  - First line: Employee EMPLOYEE_NAME is done with
    tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        - EMPLOYEE_NAME: name of the employee
        - NUMBER_OF_DONE_TASKS: number of completed tasks
        - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of
        completed and non-completed tasks
  - Second and N next lines: display the title of completed tasks: TASK_TITLE
  (with 1 tabulation and 1 space before the TASK_TITLE)
"""

import requests
import sys


def gather_data(employeeId):
    """
    Prints the employee TODO list progress
    in a certain format (see details above)
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
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    gather_data(sys.argv[1])
