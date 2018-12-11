#!/usr/bin/env python3
# Written by: Travis Norgaard
# Practice OS and Shell Utilities
## Import the shell utilities
import shutil
##
Import the OS utilities
import os
## Always start in /home/student/mycode
os.chdir('/home/student/mycode/')

## Make a copy of the existing file
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

## Make a copy of the whole directory
shutil.copytree('5g_research/', '5g_research_backup/')
