from getpass import _raw_input

__author__ = 'user'
#geting system access
import subprocess
import os
import sys

#checking super access
euid = os.geteuid()
if euid != 0:
    print ("There is no root access. Try sudo...")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # Trying to rerun this script (following process) through sudo.
    os.execlpe('sudo', *args)
print ('Root access granted - ', euid)
#using super access
#adding required packages

answer = raw_input("Owerwrite log yes or no? Default No. ").lower()
print('answer value is ', answer)
if answer == '':
    answer = "no"
    print('answer value is ',answer)
if answer == "yes" or answer == "y":
    subprocess.call('apt-get update -y > echo nfsset.log', shell=True)
    subprocess.call('apt-get install nfs-kernel-server -y >> echo nfsset.log', shell=True)
elif answer == "no" or answer == "n":
    subprocess.call('apt-get update -y >> echo nfsset.log', shell=True)
    subprocess.call('apt-get install nfs-kernel-server -y >> echo nfsset.log', shell=True)


