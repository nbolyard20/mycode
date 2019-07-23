#!/usr/bin/env python3

import requests

def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
    startrequest = input("Please enter a start date (YEAR-MONTH-DAY): ")
    startdate = 'start_date=' + startrequest
    #startdate = 'start_date=2018-06-01'
    enddate = '&end_date=END_DATE'
    mykey = '&api_key=CxYofK3XRuBUBbbQySebSG16fP7G2iaNByDHdLoy'
    
    neourl = neourl + startdate + mykey
    neojson = (requests.get(neourl)).json()

    print(neojson)

main()

