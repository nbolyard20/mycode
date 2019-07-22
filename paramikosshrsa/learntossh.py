#!/usr/bin/env python3

import os
import paramiko

def commandissue(command_to_issue, sshsession):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

def main():
    sshsession = paramiko.SSHClient()

    ########### To Use UN/PW to Authentication ############
    #sshsession.connect(server, username-username, password=password)

    ########### To Use Keys #############

    ## mykey is out private key
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    ## if we never went ot this SSH host, add the fingerprint to the known hosts file
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ## creds to connect
    sshsession.connect(hostname='10.10.2.3', username='bender', pkey=mykey)

    ## simple list of commands to issue across out connection
    our_commands = ['touch sshworked.txt', 'touch create.txt', 'touch file3.txt', 'ls']

    ## cycle through our commands on the far end
    for x in our_commands:
        print(commandissue(x, sshsession).decode('utf-8'))

main()
