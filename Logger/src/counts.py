#!/bin/python 3
#
#### filename: counts.py
#### description: Component of Logger todo utility
#### repository: git@github.com:pathologicalhandwaving/tasks.git
#### date-created: 2018-03-23
#### date-modified: 2018-03-23
####

import re


# init vars
done = 0
todo = 0

path = "/Users/Em/Repos/tasks/20728d49baac67ae2f557153e7396627/todo.md"

# read file
todolist = open(path, 'r')


# Find pattern
pattern = re.compile("-\s\[X\]\s+.*")

for line in todolist:
    if pattern.match(line):
        done = done + 1
    else:
        todo = todo + 1


print("Completed Tasks:", str(done))
print("Tasks Left ToDo:", str(todo), "\n\n")

# CHECKER
#todolist = open(path, 'r')
#for line in todolist:
#    print(line)

