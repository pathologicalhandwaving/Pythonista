#!/bin/python3
# coding: utf-8

'''
---
title: captainorg.py
date-created: 2018-03-27
date-modified: 2018-03-27
description: >
  Create daily log page for org mode
tags: org mode, python 3, captains log,
---
'''

# PACKAGES
import sys
import re
import json
from datetime import datetime, date
import time
from time import strftime
import location
from urllib import request


# VARIABLES
today ={}
today1 = {}
bulletstyles = {}
checkboxes = {}
headings = {}

# DICTIONARIES

#bulletstyles = dict({'styles': '- ', '+ ', '* ', '1. ', '1) '})

#checkboxes = dict({'checkopen': '[ ]'}, {'checkdone': '[X]'}, {'checkenum': '[/]'})

#headings = dict({'h1': '* '}, {'h2': '** '}, {'h3': '*** '}, {'h4': '**** '}, {'h5': '***** '})

## TIMESTAMP

timestamp = time.strftime(format("%Y-%m-%dT%H%M%S"))



# GET WUNDERGROUND CONDITIONS DATA
f = request.urlopen('http://api.wunderground.com/api/d0cc26c688958a0d/conditions/q/Fl/Lake_City.json')


# GET WUNDERGROUND FORECAST DATA
c = request.urlopen('http://api.wunderground.com/api/d0cc26c688958a0d/forecast/q/Fl/Lake_City.json')


# READ AND PARSE DATA
json_string = f.read()
parsed_json = json.loads(json_string)
json2_string = c.read()
parsed2_json = json.loads(json2_string)
with open('today1.json', 'w') as outfile:
    json.dump(today1, outfile)
    
with open('today.json', 'w') as outfile:
    json.dump(today, outfile)
    
currentweather = parsed_json['current_observation']['weather']
#weather = print("    Currently:", currentweather, "\n")

#print(weather)
currenttemp = parsed_json['current_observation']['temp_f']

humidity = parsed_json['current_observation']['relative_humidity']

wind_direction = parsed_json['current_observation']['wind_dir']

wind_speed = parsed_json['current_observation']['wind_mph']
wind_gust = parsed_json['current_observation']['wind_gust_mph']

wind_degree = parsed_json['current_observation']['wind_degrees']

pressure_lbin = parsed_json['current_observation']['pressure_in']

pressure_mb = parsed_json['current_observation']['pressure_mb']

dewpoint = parsed_json['current_observation']['dewpoint_f']

solar = parsed_json['current_observation']['solarradiation']

uvrad = parsed_json['current_observation']['UV']


today_precip = parsed_json['current_observation']['precip_today_in']

hour_precip = parsed_json['current_observation']['precip_1hr_in']
 
visibility = parsed_json['current_observation']['visibility_mi']


#forecast = parsed2_json['forecast']['forecastday']['period']['0']['fcttext']
#print(forecast)
# PRINT WEATHER DATA
#print("Weather:", currentweather)
#print("Temperature: ", currenttemp, "° F", sep="")
#print("Precipitation Today:", today_precip, "in")
#print("Precipitation for the Hour:", hour_precip, "in")
#print("Humidity:", humidity)
#print("Direction of Winds:", wind_direction)
#print("Degree of Direction:", wind_degree, "[3]")
#print("Wind Speed:", wind_speed, "mph")
#print("Wind Gusts:", wind_gust, "mph")
#print("Visibility:", visibility, "mi")
#print("Pressure:", pressure_mb, "mb (", pressure_lbin, "lbs/in² [1])")
#print("Solar Radiation: ", solar)
#print("UV Index:", uvrad)
uvrad = float(uvrad)







## FILENAME
filename = timestamp+".org"

## CREATE FILE
file = open(filename, "w+")

## WRITE FILE

file.write("* Captain's Log: "+ timestamp)
file.write("\n\n")
file.write("** Weather Report\n")
file.write("  Currently: ")
file.write(currentweather)
file.write("\n")
file.write("  Temperature: ")
file.write(str(currenttemp))
file.write("F")
file.write("\n")
file.write("  Pressure: ")
file.write(pressure_lbin)
file.write("\n")
file.write("  Humidity: ")
file.write(humidity)
file.write("\n")
file.write("  Precipitation: ")
file.write(today_precip)
file.write("\n")
#file.write("    UV Radiation:\n")
if (0.0 <= uvrad <= 2.9):
    file.write("  UV Index Low: ")
    file.write(str(uvrad))
    file.write("\n")
elif (3.0 <= uvrad <= 5.9 ):
    file.write("  UV Index Moderate: ")
    file.write(str(uvrad))
    file.write("\n")
elif ( 6.0 <= uvrad <= 7.9):
    file.write("  UV Index High: ")
    file.write(str(uvrad))
    file.write("\n")
elif ( 8.0 <= uvrad <= 10.9 ):
    file.write("  UV Index Very High: ")
    file.write(str(uvrad))
    file.write("\n")
else:
    file.write("  UV Index Extreme: ")
    file.write(str(uvrad))
    file.write("\n")

file.write("\n")
file.write("** Events Today\n")
file.write("*** Event 1:\n")
file.write("    Description:\n")
file.write("    Time:\n")
file.write("    Ends:\n\n")
file.write("*** Event 2:\n")
file.write("    Description:\n")
file.write("    Time:\n")
file.write("    Ends:\n")
file.write("\n\n")
file.write("** Todo: [/]\n")
file.write("  - [ ] Thing one\n")
file.write("  - [ ] Thing two\n")
file.write("  - [ ] Thing three\n")
file.write("\n\n")
file.write("** Notes\n")
file.write("  + \n")
file.write("  + \n")
file.write("  + \n")
file.write("\n")
file.write("** Tommorow:\n")
file.write("  + \n")
file.write("  + \n")
file.write("  + \n")
file.write("\n")


# PRINT STATEMENTS

print(filename)

# CLOSE FILE
file.close()