__author__ = 'Admin'

import os
import sys
import subprocess

# checking super access
euid = os.geteuid()
if euid != 0:
    print ("There is no root access. Try sudo...")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # Trying to rerun this script (following process) through sudo.
    os.execlpe('sudo', *args)
print ('The effective user identifier is ', euid)
# Restoring list of export
___log_path = ((os.path.abspath(__file__).replace(('/documentation/preconditions/' + os.path.basename(__file__)), '/logs/')))
subprocess.call('cp /etc/exports.back /etc/exports')
subprocess.call('sudo rmdir /nfs')
subprocess.call('sudo service nfs restart')
# Purging NFS server
subprocess.call('date | tee -a %snfsset.log'% ___log_path, shell=True)
subprocess.call('apt-get update -y | tee -a %snfsset.log', shell=True)
subprocess.call('apt-get purge nfs-kernel-server -y nfs-common -y | tee -a %snfsset.log'% ___log_path, shell=True)