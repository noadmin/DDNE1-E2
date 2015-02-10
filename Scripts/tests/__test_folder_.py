__author__ = 'Admin'
# Going in /nfs direction
import unittest
import os

class TestDirectory(unittest.TestCase):
#Let do some preparations

    def setUp(self):
        if os.path.exists('new_dir'):
            os.rmdir('new_dir')
        if not os.path.exists('rem_dir'):
            os.mkdir('rem_dir')
        if not os.path.exists('old_name_dir'):
            os.mkdir('old_name_dir')
        if not os.path.exists('owner_dir'):
            os.mkdir('owner_dir')
        if not os.path.exists('permissions_dir'):
            os.mkdir('permissions_dir')

    def tearDown(self):
        if os.path.exists('new_dir'):
            os.rmdir('new_dir')
        if os.path.exists('rem_dir'):
            os.rmdir('rem_dir')
        if os.path.exists('new_name_dir'):
            os.rmdir('new_name_dir')
        if os.path.exists('owner_dir'):
            os.rmdir('owner_dir')
        if os.path.exists('permissions_dir'):
            os.rmdir('permissions_dir')

    def test_crate(self):
        try:
            self.assertFalse(os.path.exists('new_dir'), '')
            os.mkdir('new_dir')
            self.assertTrue(os.path.exists('new_dir'))
        except:
            self.fail('directory wasn\'t created')

    def test_remove(self):
        try:
            self.assertTrue(os.path.exists('rem_dir'))
            os.rmdir('rem_dir')
            self.assertFalse(os.path.exists('rem_dir'))
        except:
            self.fail('directory wasn\'t remowed')

    def test_rename(self):
        try:
            self.assertTrue(os.path.exists('old_name_dir'))
            os.rename('old_name_dir', 'new_name_dir')
            self.assertTrue(os.path.exists('new_name_dir'))
            self.assertFalse(os.path.exists('old_name_dir'))
        except:
            self.fail('directory wasn\'t renamed')

    def test_ch_owner(self):
        try:
            self.assertTrue('owner_dir')
            os.chown('owner_dir', 1, 1)
        except:
            self.fail('failded to change owner')
    def test_ch_permissions(self):
        try:
            self.assertTrue('permissions_dir')
            os.chmod('permissions_dir', 0o777)
        except:
            self.fail('failed to change permissions')



if __name__ == '__main__':
    log_file = 'log_file.txt'
    f = open(log_file, 'w')
    runner = unittest.TextTestRunner(f, verbosity=2)
    unittest.main(testRunner=runner)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestDirectory)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    # runner = unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main(testRunner=runner)