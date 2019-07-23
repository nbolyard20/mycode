#!/usr/bin/env python3

"""Tracking ISS"""

import urllib.request
import json

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    ## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)

    ## put fileobject into helmet
    helmet = groundctrl.read()

    ## decode json to python data structure
    helmetson = json.loads(helmet.decode('utf-8'))

    ## display our pythonic data
    #print("\n\nConverted python data")
    #print(helmetson)

    print("\n\nPeople in Space: ", helmetson['number'])
    people = helmetson['people']
    #print(people)


    for person in people:
        print(person['name'] + " on the " + person['craft'])

main()
