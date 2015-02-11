__author__ = 'noadmin'

import unittest
import os
import random

# Trying to change file owner

class TC007(unittest.TestCase):
    def setUp(self):
        if not os.path.exists('test_file'):
            test_file = open('test_file', 'w')
            random_sequence = random.getrandbits(8388608)
            test_file.write(random_sequence)
            test_file.close()

    def tearDown(self):
        if os.path.exists('test_file'):
            os.remove('test_file')

    def testChangingFileUserOwner(self):
        current_user = os.getuid()
        old_owner = os.stat('test_file').st_uid
        try:
            # Check who is the owner
            if old_owner == '0':
                # set owner to current user
                os.chown('test_file', uid=current_user)
            else:
                # set owner to root
                os.chown('test_file', uid='0')
            self.assertNotEqual(os.stat('test_file').st_uid, old_owner)
        except:
            self.fail('File owner user change failed')


# Trying to change file owner group

class TC008(unittest.TestCase):
    def setUp(self):
        if not os.path.exists('test_file'):
            test_file = open('test_file', 'w')
            random_sequence = random.getrandbits(8388608)
            test_file.write(random_sequence)
            test_file.close()

    def tearDown(self):
        if os.path.exists('test_file'):
            os.remove('test_file')

    def testChangingFileGroupOwner(self):
        current_group = os.getgid()
        old_owner = os.stat('test_file').st_gid
        try:
            # Check who is the owner
            if old_owner == '0':
                # set owner to current user group
                os.chown('test_file', gid=current_group)
            else:
                # set owner to root
                os.chown('test_file', gid='0')
            self.assertNotEqual(os.stat('test_file').st_gid, old_owner)
        except:
            self.fail('File owner group change failed')


# Trying to change folder owner

class TC009(unittest.TestCase):
    def setUp(self):
        if not os.path.exists('test_folder'):
            os.mkdir('test_folder')

    def tearDown(self):
        if os.path.exists('test_folder'):
            os.rmdir('test_folder')

    def testChangingFolderUserOwner(self):
        current_user = os.getuid()
        old_owner = os.stat('test_folder').st_uid
        try:
            # Check who is the owner
            if old_owner == '0':
                # set owner to current user
                os.chown('test_folder', uid=current_user)
            else:
                # set owner to root
                os.chown('test_folder', uid='0')
            self.assertNotEqual(os.stat('test_folder').st_uid, old_owner)
        except:
            self.fail('Folder owner user change failed')


# Trying to change folder owner group

class TC010(unittest.TestCase):
    def setUp(self):
        if not os.path.exists('test_folder'):
            os.mkdir('test_folder')

    def tearDown(self):
        if os.path.exists('test_folder'):
            os.rmdir('test_folder')

    def testChangingFolderGroupOwner(self):
        current_group = os.getgid()
        old_owner = os.stat('test_folder').st_gid
        try:
            # Check who is the owner
            if old_owner == '0':
                # set owner to current users group
                os.chown('test_folder', gid=current_group)
            else:
                # set owner to root
                os.chown('test_file', gid='0')
            self.assertNotEqual(os.stat('test_folder').st_gid, old_owner)
        except:
            self.fail('Folder owner group change failed')