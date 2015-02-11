__author__ = 'noadmin'

# import necessary dependencies

import unittest
import os
import random

# Trying to change content in target folder
# To perform fully qualified test we must check base permissions
# Trying to create folder in target directory

class TC001(unittest.TestCase):

# Let do some preparing for test and clean up after by overriding setUp and tearDown methods
# Frankly speaking, it's no good steps (because it's broken of encapsulation of the test case)
# but it necessary for single-use of this test. I'm so sorry...

    def setUp(self):
        if os.path.exists('test_folder'):
            os.rmdir('test_folder')

    def tearDown(self):
        if os.path.exists('test_folder'):
            os.rmdir('test_folder')

    def testCreateFolder(self):
        try:
            self.assertFalse(os.path.exists('test_folder'))
            os.mkdir('test_folder')
            self.assertTrue(os.path.exists('new_test_dir'))
        except:
            self.fail(self, 'Failed to create folder')


# Trying to delete folder

class TC002(unittest.TestCase):

# Same problem with encapsulation

    def setUp(self):
        if not os.path.exists('test_folder'):
            os.mkdir('test_folder')

    def testDeleteFolder(self):
        try:
            self.assertTrue(os.path.exists('test_folder'))
            os.rmdir('test_folder')
            self.assertFalse(os.path.exists('test_folder'))
        except:
            self.fail(self, 'Failed to delete folder')


# Trying to create test file with random content

class TC003(unittest.TestCase):

    def setUp(self):
        if os.path.exists('test_file'):
            os.remove('test_file')

    def testCreateFile(self):
        try:
            test_file = open('test_file', 'w')
            random_sequence = random.getrandbits(8388608)
            test_file.write(random_sequence)
            test_file.close()
            self.assertEquals(random_sequence, test_file.read())
            test_file.close()
        except:
            self.fail('file wasn\'t created')


# Trying to modify content of test file

class TC004(unittest.TestCase):

    def setUp(self):
        if not os.path.exists('test_file'):
            test_file = open('test_file', 'w')
            random_sequence = random.getrandbits(8388608)
            test_file.write(random_sequence)
            test_file.close()

    def testModifyFile(self):
        try:
            test_file = open('test_file', 'w')
            old_text = test_file.read()
            random_sequence = random.getrandbits(8388608)
            test_file.write(random_sequence)
            test_file.close()

            test_file = open('test_file', 'r')
            self.assertEquals(random_sequence, test_file.read())
            self.assertNotEquals(old_text, test_file.read())
            test_file.close()

        except:
            self.fail('file wasn\'t edited')


# Trying to delete file

class TC005(unittest.TestCase):

    def setUp(self):
        if not os.path.exists('test_file'):
            test_file = open('test_file', 'w')
            random_sequence = random.getrandbits(8388608)
            test_file.write(random_sequence)
            test_file.close()

    def testDeleteFile(self):
        try:
            self.assertTrue(os.path.exists('test_file'))
            os.remove('test_file')
            self.assertFalse(os.path.exists('test_file'))
        except:
            self.fail('file was\'t deleted')


# Trying to rename test file

class TC006(unittest.TestCase):

    def setUp(self):
        if not os.path.exists('test_file'):
            test_file = open('test_file', 'w')
            random_sequence = random.getrandbits(8388608)
            test_file.write(random_sequence)
            test_file.close()

    def tearDown(self):
        if os.path.exists('test_file_new'):
            os.remove('test_file_new')
        if os.path.exists('test_file'):
            os.remove('test_file')

    def testRenameFile(self):
        try:
            os.path.exists('test_file')
            os.rename('test_file', 'test_file_new')
            self.assertTrue(os.path.exists('test_file_new'))
            self.assertFalse(os.path.exists('test_file'))
        except:
            self.fail('file wasn\'t renamed')