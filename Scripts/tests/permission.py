__author__ = 'noadmin'

import unittest
import os
import random

# Trying to change file permissions

class TC011(unittest.TestCase):
    def setUp(self):
        if not os.path.exists('test_file'):
            test_file = open('test_file', 'w')
            random_sequence = random.getrandbits(8388608)
            test_file.write(random_sequence)
            test_file.close()

    def tearDown(self):
        if os.path.exists('test_file'):
            os.remove('test_file')


# Trying to determinate and change file read access
# Because default file mode is 0777 we can skip full determination of access mode
# determine whether the file is available to read and change the setting to the opposite

    def testChangingFileReadPermissions(self):
        if os.access('test_file', os.R_OK):
            try:
                os.chmod('test_file', 0333)
                self.assertFalse(os.access('test_file', os.R_OK))
            except:
                self.fail('Failed to change read permission')
        else:
            try:
                os.chmod('test_file', 0777)
                self.assertTrue(os.access('test_file', os.R_OK))
            except:
                self.fail('Failed to change read permission')

# determine whether the file is available to write and change the setting to the opposite

    def testChangingFileWritePermissions(self):
        if os.access('test_file', os.W_OK):
            try:
                os.chmod('test_file', 0555)
                self.assertFalse(os.access('test_file', os.W_OK))
            except:
                self.fail('Failed to change write permission')
        else:
            try:
                os.chmod('test_file', 0777)
                self.assertTrue(os.access('test_file', os.W_OK))
            except:
                self.fail('Failed to change write permission')

# determine whether the file is available to execute and change the setting to the opposite

    def testChangingFileExecutePermissions(self):
        if os.access('test_file', os.X_OK):
            try:
                os.chmod('test_file', 0666)
                self.assertFalse(os.access('test_file', os.X_OK))
            except:
                self.fail('Failed to change execute permission')
        else:
            try:
                os.chmod('test_file', 0777)
                self.assertTrue(os.access('test_file', os.X_OK))
            except:
                self.fail('Failed to change execute permission')
            self.fail('Execute permission change failed')