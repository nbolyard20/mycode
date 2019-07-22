#!/usr/bin/env python3

##Moving files with SFTP

import paramiko
import os

## where to connect to
t = paramiko.Transport("10.10.2.3", 22) 

## how to connect
t.connect(username='bender', password='alta3')

## make a connection
sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files
for x in os.listdir("/home/student/filestocopy/"):
    if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connection
sftp.close()
