__author__ = 'Admin'

#import necessary dependencies
import unittest
import os
import random

# To perform fully qualified test we must check base permissions
# Trying to create folder in target directory
class TC001(unittest.TestCase):
# Let do some preparing for test and clean up after
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
            self.fail(self,'Failed to create folder')


# Trying to delete created folder
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
            self.fail(self,'Failed to delete folder')

# Trying to create file with random content
class TC003(unittest.TestCase):
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
    def test_append(self):
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

#Test block for run test suite
if __name__ == '__main__':
    log_file = 'log_file.txt'
    f = open(log_file, 'w')
    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TC001)
    # unittest.TextTestRunner(verbosity=2).run(suite)