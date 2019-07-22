#!/usr/bin/env python3

import shutil
import os


os.chdir('/home/student/mycode') #forces program to 'start' in home user directory
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy') #copies a file
shutil.copytree('5g_research/', '5g_research_backup/') #copies a directory
