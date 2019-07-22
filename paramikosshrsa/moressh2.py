#!/usr/bin/env python3

"""Learning about Python SSH"""

import warnings
import paramiko

#filter out warnings with the word paramiko
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

def main():
    """Our runtime code that calls other functions"""
    # describe the connection data
    #credz = [{'un': 'bender', 'ip': '10.10.2.3'}, {'un': 'zoidberg', 'ip': '10.10.2.5'},\
    #        {'un': 'fry', 'ip': '10.10.2.4'}]
    credz = []
    with open('credz.txt', 'r') as credentials:
        for sline in credentials: #single line from our file is sline
            credentials.append(sline.rstrip("\n").split(' '))
    
    # MORE WORK HERE TO READ FROM FILES
    
    
    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    # loop across credz
    for cred in credz:
        ## create session object
        sshsession = paramiko.SSHClient()

        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ## display conections
        print ("Connecting to... " + cred.get('un') + "@" + cred.get('ip'))

        ## make connection
        sshsession.connect(hostname=cred.get('ip'), username=cred.get('un'), pkey=mykey)

        ## touch the filw goodnews.everyone in home directory
        sshsession.exec_command("touch /home/" + cred.get('un') + "/goodnews.everyone")

        ## list the connections of home directory
        sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get('un'))

        ## display output
        print(sessout.read().decode('utf-8'))

        ## close / cleanup SSH connection
        sshsession.close()

    print("Thanks for looping with Alta3")

main()
