#!/usr/bin/env python3

import urllib.request
import json
import webbrowser

## Define APOD
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=CxYofK3XRuBUBbbQySebSG16fP7G2iaNByDHdLoy'

## Call webservice
apodurlobj = urllib.request.urlopen(apodurl + mykey)

## read the object
apodread = apodurlobj.read()

## decode json
decodeapod = json.loads(apodread.decode('utf-8'))

print('\n\nConverted python data')
print(decodeapod)

## user firefox to open
input('\nPress Enter to open NASA Picture of the Day in Firefox')
webbrowser.open(decodeapod['url'])
