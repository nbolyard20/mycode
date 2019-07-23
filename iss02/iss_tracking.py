#!/usr/bin/env python3

import urllib.request
import json
import turtle
import time

## Trace the ISS
eoss = 'http://api.open-notify.org/iss-now.json'

## Call the web server
trackiss = urllib.request.urlopen(eoss)

## put into the file object
ztrack = trackiss.read()

## json to python
result = json.loads(ztrack.decode('utf-8'))

## display python data
print("\n\nConverted data")
print(result)
input('\nISS data retrieved & converted. Press any key to continue.')

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen() #create a screen object
screen.setup(720, 360) # set resolution
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('iss_map.gif')

## register the tiny ISS gif
screen.register_shape('spriteiss.gif')
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

## My location
yellowlat = 39.2
yellowlon = -80.1
mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color('yellow')
mylocation.goto(yellowlon, yellowlat)
mylocation.dot(5)
mylocation.hideturtle()

## move the tiny ISS
lon = round(float(lon))
lat = round(float(lat))
iss.penup()
iss.goto(lon, lat)

## call for the data of ISS pass over location
passiss = 'http://api.open-notify.org/iss-pass.json'
passiss = passiss + '?lat=' + str(yellowlat) + '&lon=' + str(yellowlon)
response = urllib.request.urlopen(passiss)
result = json.loads(response.read().decode('utf-8'))

##print(result)

## grab the first passover time
over= result['response'][1]['risetime']
## set the font on map
style = ('Arial', 6, 'bold')
mylocation.write(time.ctime(over), font=style)

turtle.mainloop() # SHOULD ALWAYS BE AT BOTTOM OF CODE

