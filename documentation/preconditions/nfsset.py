__author__ = 'user'
#geting system access
import subprocess
import os
import sys

#checking super access
euid = os.geteuid()
if euid != 0:'''
    print ("There is no root access. Try sudo...")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # Trying to rerun this script (following process) through sudo.
    os.execlpe('sudo', *args)'''
    os.popen('echo 12345678 | sudo -s')
print ('Root access granted - ', euid)
#get super access

subprocess.call('apt-get update', shell=True)