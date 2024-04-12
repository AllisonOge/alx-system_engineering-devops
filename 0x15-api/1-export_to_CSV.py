#!/usr/bin/python3
"""
Task 1: Export to CSV

Expand the `0-get_data_from_an_API.py` script to export the data to a CSV file.

Requirements:
- Records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv
"""

import requests
import sys
import csv


def main(employeeId):
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
    filename = "{}.csv".format(employeeId)
    with open(filename, mode="w", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employeeId, name, task.get("completed"),
                             task.get("title")])


if __name__ == "__main__":
    main(sys.argv[1])
