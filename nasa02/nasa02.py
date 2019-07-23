#!/usr/bin/env python3

import urllib.request
import json

neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'state_date=2018-06-01'
enddate = '&end_date=END_DATE'
mykey = '&api_key=CxYofK3XRuBUBbbQySebSG16fP7G2iaNByDHdLoy'

neourl = neourl + startdate + mykey
neourlobj = urllib.request.urlopen(neourl)
neoread = neourlobj.read()
decodeneo = json.loads(neoread.decode('utf-8'))
print('\nConvverted python')
print(decodeneo)

