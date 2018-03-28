#!/bin/python 3
#
#### filename: counts.py
### version: mobile
#### description: Component of Logger todo utility
#### repository: git@github.com:pathologicalhandwaving/tasks.git
#### date-created: 2018-03-23
#### date-modified: 2018-03-23
####

import re


# init vars
done = 0
todo = 0

path = "todo.md"

# read file
todolist = open(path, 'r')


# Find pattern
string = re.compile("-\s\[X\]\s+.*")
#result = string.match()
pattern = re.compile("-\s[\s]\s+.*")

for line in todolist:
    if string.match(line):
        done = done + 1
    else:
        todo = todo + 1
        print(line)



#def displayMatch(match):
    
    
print("Completed Tasks:", str(done))
print("Tasks Left ToDo:", str(todo), "\n\n")

todolist.close()
# CHECKER
#todolist = open(path, 'r')
#for line in todolist:
#    print(line)



