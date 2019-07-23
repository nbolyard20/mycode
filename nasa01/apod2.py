#!/usr/bin/env python3

import urllib.request
import json
import webbrowser
from pprint import pprint as pp # of the standard library

NASAAPI = 'https://api.nasa.gov/planetary/apod?'
MYKEY = 'api_key=CxYofK3XRuBUBbbQySebSG16fP7G2iaNByDHdLoy'

##print pretty json
def main():
    """run-time code"""
    nasaapiobj = urllib.request.urlopen(NASAAPI + MYKEY)
    nasaread = nasaapiobj.read()
    convertedjson = json.loads(nasaread.decode('utf-8'))

    print(convertedjson)
    input('\nThis is converted JSON. Press ENTER to continue.')
    pp(convertedjson)
    #pprint.pprint(convertedjson) #if you do a simple import pprint
    input('\nThis is the pretty printed JSON. Press ENTER to continue.')

    # Print the desciption of the photo we are viewing
    print(convertedjson['explanation'])
    input('\nPress Enter to view this photo of the day')

    webbrowser.open(convertedjson['hdurl'])


main()
