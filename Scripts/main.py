__author__ = 'noadmin'

import unittest
from tests import owner
from tests import content
from tests import permission

# Main test runner

if __name__ == '__main__':

    # Collecting Tests Suits by functional

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
    # ownerTestSuite.addTests(unittest.makeSuite(owner.TC009))
    # ownerTestSuite.addTests(unittest.makeSuite(owner.TC010))

    permissionTestSuite = unittest.TestSuite()
    permissionTestSuite.addTests(unittest.makeSuite(permission.TC011))

    # Collecting all Test Suits in main object for general use

    alltests = unittest.TestSuite([contentTestSuite, ownerTestSuite, permissionTestSuite])

    # Setting up logging parameters and run

    log_file = 'log_file.txt'
    f = open(log_file, 'w')
    runner = unittest.TextTestRunner(f, verbosity=2)
    runner.run(alltests)

    # Short summary =)

    print(open(log_file).read())