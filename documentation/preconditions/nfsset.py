from getpass import _raw_input

__author__ = 'user'
#geting system access
import subprocess
import os
import sys

# checking super access
euid = os.geteuid()
if euid != 0:
    print ("There is no root access. Try sudo...")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # Trying to rerun this script (following process) through sudo.
    os.execlpe('sudo', *args)
print ('The effective user identifier is ', euid)
# using super access
# adding required packages for NSF server and client
# getting absolute path to log folder
# I can use os.getcwd() but who's know =) let me be die hard...
___log_path = ((os.path.abspath(__file__).replace(('/documentation/preconditions/' + os.path.basename(__file__)), '/logs/')))
# choosing between installation and uninstallation NFS
def choice():
    print("Step 1")
    print('For installing NFS hit 1')
    print('For uninstall NFS hit 2')
    print('For skipping these step hit 3 or leave it empty')
    answer = raw_input("Do you choice and press \"Enter\" ")

    if answer == "1":
        subprocess.call('date | tee -a %snfsset.log'% ___log_path, shell=True)
        subprocess.call('apt-get update -y | tee -a %snfsset.log'% ___log_path, shell=True)
        subprocess.call('apt-get install nfs-kernel-server -y nfs-common -y | tee -a %snfsset.log'% ___log_path, shell=True)

    elif answer == "2":
        subprocess.call('date | tee -a %snfsset.log'% ___log_path, shell=True)
        subprocess.call('apt-get update -y | tee -a %snfsset.log', shell=True)
        subprocess.call('apt-get purge nfs-kernel-server -y nfs-common -y | tee -a %snfsset.log'% ___log_path, shell=True)
        exit()

    elif answer == '' or answer == "3":
        print('Step 1 is skipped')

    else:
        print("Incorrect input! Try again.")
        choice()
choice()
#Settind up server configuration
print('Step 2')





