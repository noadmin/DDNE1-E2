__author__ = 'noadmin'

import unittest
import os
from tests import owner
from tests import content
from tests import permission

# Main test runner
# do not forget to add tests
# we should get root access to perform testing

# euid = os.geteuid()
# if euid != 0:
#     print ("There is no root access. Try sudo...")
#     args = ['sudo', sys.executable] + sys.argv + [os.environ]
#     # Trying to rerun this script (following process) through sudo.
#     os.execlpe('sudo', *args)
# print ('The effective user identifier is ', euid)

#root access granted and we can run tests
if __name__ == '__main__':

    contentTestSuite = unittest.TestSuite()
    contentTestSuite.addTests(unittest.makeSuite(content.TC001))
    contentTestSuite.addTests(unittest.makeSuite(content.TC002))
    contentTestSuite.addTests(unittest.makeSuite(content.TC003))
    contentTestSuite.addTests(unittest.makeSuite(content.TC004))
    contentTestSuite.addTests(unittest.makeSuite(content.TC005))
    contentTestSuite.addTests(unittest.makeSuite(content.TC006))

    ownerTestSuite = unittest.TestSuite()
    ownerTestSuite.addTests(unittest.makeSuite(owner.TC007))
    ownerTestSuite.addTests(unittest.makeSuite(owner.TC008))
    ownerTestSuite.addTests(unittest.makeSuite(owner.TC009))
    ownerTestSuite.addTests(unittest.makeSuite(owner.TC010))

    permissionTestSuite = unittest.TestSuite()
    permissionTestSuite.addTests(unittest.makeSuite(permission.TC011))

    alltests = unittest.TestSuite([contentTestSuite, ownerTestSuite, permissionTestSuite])


    # log = open('log', 'w')
    #
    # alltests.run(debug=False)

    log_file = 'log_file.txt'
    f = open(log_file, 'w')
    runner = unittest.TextTestRunner(f)
    runner.run(alltests)