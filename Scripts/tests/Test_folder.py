__author__ = 'Admin'
# Going in /nfs direction
import unittest
import os

class Test_directory(unittest.TestCase):

    def test_crate(self):
        try:
            os.mkdir('test_dir')
            os.chdir('test_dir')
        except:
            self.fail('directory wasn\'t created')

    def test_remove(self):
        try:
            os.rmdir('test_dir')
        except:
            self.fail('directory wasn\'t remowed')


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)