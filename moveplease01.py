#!/usr/bin/env python3
# Move a file and rename a file
## Import shell utilities module
import shutil
## Import OS module
import os
## Make or set the base dir
os.chdir('/home/student/mycode/')
## Move a file in the base dir to ceph_storage dir
shutil.move('raynor.obj', 'ceph_storage/')
## Read new name for a file
xname = input('What is the new name for kerrigan.obj? ')
## Rename the file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
