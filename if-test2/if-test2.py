#!/usr/bin/env python3

ipchk = input('Apply an IP address: ') # this line now prompts the user for input

if ipchk== '192.168.70.1': # if any info is provided it is true
    print('Look likes the Gateway was set: ' + ipchk + '. This is not recommended.')
elif ipchk: #if and data is provided, this is true
    print('Looks like the IP address was set: ' + ipchk)
else: #if no data
    print('You did not provide input.')


