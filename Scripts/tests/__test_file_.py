__author__ = 'Admin'

import unittest
import random
import os

class Test_file(unittest.TestCase):

    def test_create(self):
        try:
            test_file = open('test_file', 'w')
            random_sequence = random.getrandbits('8388608')
            test_file.write(random_sequence)
            test_file.close()
            self.assertEquals(random_sequence, test_file.read())
            test_file.close()

        except:
            self.fail('file wasn\'t created')

    def test_append(self):
        try:

            test_file = open('test_file', 'w')
            old_text = test_file.read()
            random_sequence = random.getrandbits('8388608')
            test_file.write(random_sequence)
            test_file.close()

            test_file = open('test_file', 'r')
            self.assertEquals(random_sequence, test_file.read())
            self.assertNotEquals(old_text, test_file.read())
            test_file.close()

        except:
            self.fail('file wasn\'t edited')

    def test_delete(self):
        try:
            os.remove('test_file')
            self.assertFalse(os.exists('test_file'))
        except:
            self.fail('file wasn\'t deleted')

    def test_rename(self):
        try:
            os.rename('test_file', 'test_file_new')
            self.assertTrue(os.path.exists('test_file_new'))
        except:
            self.fail('file wasn\'t renamed')

    def test_replace(self):
        try:
            os.replace('test_file', 'new_test_file')
            self.assertTrue('new_test_file')
        except:
            self.fail('file wasn\'t replaced')

    def test_ch_owner(self):
        try:
            os.chown('test_file', '1000', '1000')
            #os.ch
        except:
            self.fail('owner wasn\'t changed')

    def test_ch_permission(self):
        try:
            os.chmod('test_file', '777')
            #do something with permissions
        except:
            self.fail('permissions wasn\'t changed')


