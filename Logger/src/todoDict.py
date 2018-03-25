#!/bin/python3
###
# ---
# filename: todoDict.py
# date-created: 2018-03-23
# description: Create dict for todo instead of plain md then export as md
# ---

from datetime import date, time



# Timestamps
timestart = date.now()
pause = date.now()
unpause = date.now()
timedone = date.now()


statuscodes = {}
dates = {}
marks = {}
items = {}

marks = dict( ['undone': '- [ ] '], ['done': '- [X] '] )

dates = dict( ['date-created': 'timestart'], ['date-completed': 'timedone'], ['deactivate': 'pause'], ['reactivate': 'unpause'] )

statuscodes = dict( ['status': 'initialized', 'active', 'complete', 'inprogress', 'blocked', 'inactive', 'planning', 'scheduled', 'dependent-task'] )

areas = dict( ['area': 'family', '

