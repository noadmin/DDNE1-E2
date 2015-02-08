__author__ = 'Admin'
# Going in /nfs direction
import unittest
import os


class TestDirectory(unittest.TestCase):

    def setUp(self):
        if os.path.exists('new_dir'):
            os.rmdir('new_dir')
        if os.path.exists('rem_dir') == False:
            os.mkdir('rem_dir')

    def test_crate(self):
        try:
            self.assertFalse('new_dir')
            os.mkdir('new_dir')
            self.assertTrue(os.path.exists('new_dir'))
        except:
            self.fail('directory wasn\'t created')

    def test_remove(self):
        try:
            self.assertTrue(os.path.exists('rem_dir'))
            os.rmdir('test_dir')
            self.assertFalse(os.path.exists('test_dir'))
        except:
            self.fail('directory wasn\'t remowed')

    def test_rename(self):
        try:
            os.mkdir('test_dir')
            self.assertTrue(os.path.exists('test_dir'))
            os.rename('test_dir', 'new_test_dir')
            self.assertTrue(os.path.exists('new_test_dir'))
            self.assertFalse(os.path.exists('test_dir'))
        except:
            self.fail('directory wasn\'t renamed')
        os.rmdir('new_test_dir')

    def test_ch_owner(self):
        try:
            os.mkdir('test_dir')
            os.chown('test_dir', '1000', '1000')
        except:
            self.fail('failded to change owner')
        os.rmdir('test_dir')

    def test_ch_permissions(self):
        try:
            os.mkdir('test_dir')
            os.chmod('test_dir', '777')
        except:
            self.fail('failed to change permissions')
        os.rmdir('test_dir')


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)