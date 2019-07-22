#!/usr/bin/env python3

proto= ['ssh', 'http', 'https']
print(proto)
protoa= ['ssh', 'http', 'https']

proto.append('dns') # this line will add 'dns to the end of the list
protoa.append('dns') # this line will add 'dns to the end of the list
print(proto)
proto2= [22, 80, 443, 53 ] # a list of ports
proto.extend(proto2) # pass proto2 as an argument to extend method -- then print
print(proto)
protoa.append(proto2) # pass proto2 as an argument ot append method -- then print
print(protoa)
