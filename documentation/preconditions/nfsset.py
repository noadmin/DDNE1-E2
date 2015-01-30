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
__path = (os.path.abspath(__file__).replace(os.path.basename(__file__), ''))
answer = raw_input("Owerwrite log yes or no? Default No. ").lower()
print('answer value is ', answer)
if answer == '':
    answer = "no"
    print('answer value is ',answer)
    print('file is ',__file__)
    print('name is ',__name__)
    print('basename is ', os.path.basename(__file__))
    print(os.path.dirname(__file__)+'/')
    print('voodoo',(os.path.abspath(__file__).replace(os.path.basename(__file__), '') + 'nfsset.log'))
if answer == "yes" or answer == "y":
    subprocess.call('date ', '| ', 'tee nfsset.log', shell=True)
    """subprocess.call('apt-get update -y | tee -a nfsset.log', shell=True)
    subprocess.call('apt-get install nfs-kernel-server -y | tee -a nfsset.log', shell=True)
    #subprocess.call('mv -f nfsset.log ../../logs/', shell=True)"""
elif answer == "no" or answer == "n":
    subprocess.call('date | tee -a %s' % (os.path.abspath(__file__).replace(os.path.basename(__file__), '') + '/nfsset.log'), shell=True)
    """subprocess.call('apt-get update -y | tee -a nfsset.log', shell=True)
    subprocess.call('apt-get install nfs-kernel-server -y | tee -a nfsset.log', shell=True)
    #subprocess.call('mv -i nfsset.log ../../logs/', shell=True)"""



