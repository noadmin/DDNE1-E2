__author__ = 'noadmin'

import unittest
import os
import sys

# Main test runner
# do not forget to add tests
# we should get root access to perform testing

euid = os.geteuid()
if euid != 0:
    print ("There is no root access. Try sudo...")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # Trying to rerun this script (following process) through sudo.
    os.execlpe('sudo', *args)
print ('The effective user identifier is ', euid)

#root access granted and we can run tests
if __name__ == '__main__':
    log_file = 'logs/log_file.txt'
    f = open(log_file, 'w')
    runner = unittest.TextTestRunner(f, verbosity=2)
    unittest.main(testRunner=runner)