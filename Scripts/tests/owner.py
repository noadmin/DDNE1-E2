__author__ = 'noadmin'

import unittest
import os
import random

# Trying to change file owner

class TC007(unittest.TestCase):
    def setUp(self):
        if not os.path.exists('test_file'):
            content = str(random.getrandbits(888))
            test_file = open('test_file', 'w')
            test_file.write(content)
            test_file.close()

    def tearDown(self):
        if os.path.exists('test_file'):
            os.remove('test_file')

    def testChangingFileUserOwner(self):
        self.assertTrue(os.path.exists('test_file'))
        current_user = os.getuid()
        current_group = os.getgid()
        old_owner = os.stat('test_file').st_uid
        try:
            # Check who is the owner
            if old_owner == '0':
                # set owner to current user
                os.chown('test_file', current_user, current_group)
            else:
                # set owner to root
                os.chown('test_file', 0, 0)
            self.assertNotEqual(os.stat('test_file').st_uid, old_owner)
        except:
            self.fail('File owner user change failed')

# Trying to change folder owner

class TC008(unittest.TestCase):
    def setUp(self):
        if not os.path.exists('test_folder'):
            os.mkdir('test_folder')

    def tearDown(self):
        if os.path.exists('test_folder'):
            os.rmdir('test_folder')

    def testChangingFolderUserOwner(self):
        self.assertTrue(os.path.exists('test_folder'))
        current_user = os.getuid()
        current_group = os.getgid()
        old_owner = os.stat('test_folder').st_uid
        try:
            # Check who is the owner
            if old_owner == '0':
                # set owner to current user
                os.chown('test_folder', current_user, current_group)
            else:
                # set owner to root
                os.chown('test_folder', 0, 0)
            self.assertNotEqual(os.stat('test_folder').st_uid, old_owner)
        except:
            self.fail('Folder owner user change failed')