__author__ = 'Admin'

#import necessary dependencies
import unittest
import os

class TestFolder(unittest.TestCase):

    #Do some preparation before testing
    def setUp(self):
        if not os.path.exists('test_folder'):
            os.mkdir('test_folder')

    #Do some cleanup after test
    def tearDown(self):
        if os.path.exists('test_folder'):
            os.rmdir('test_folder')
        if os.path.exists('new_test_folder'):
            os.rmdir('new_test_folder')

    #Implementing test cases
    #TC001 Trying to create folder


    def test_create(self):
        try:
            self.assertFalse(os.path.exists('new_test_folder'))
            os.mkdir('new_test_dir')
            self.assertTrue(os.path.exists('new_test_dir'),'TC001 Passed: Folder created')
        except:
            self.fail(self,'TC001 Failed: Failed to create folder')

#Test block for run test suite
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFolder)
    unittest.TextTestRunner(verbosity=2).run(suite)