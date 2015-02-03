__author__ = 'Admin'

import unittest
import os

class Test_file(unittest.TestCase):

    def test_create(self):
        try:
            file = open('test_file', 'w')
            file.write('test content')
            file.close()
            if os.path.exists('test_file') == False:
                self.fail('file wasn\'t created')
        except:
            self.fail('file wasn\'t created')

    def test_append(self):
        try:
            file = open('test_file', 'a')
            file.write('another content')
            file.close()
            #if file.read(): resume from thise point =)
        except:
            self.fail('file append failed')

    def test_delete(self):
        try:
            os.remove('test_file')
        except:
            self.fail('file wasn\'t deleted')

    def test_rename(self):
        try:
            os.rename('test_file', 'test_file_new')
        except:
            self.fail('file wasn\'t renamed')

    def test_replace(self):
        try:
            os.replace('test_file', 'new_test_file')
        except:
            self.fail('file wasn\'t replaced')

    def test_ch_owner(self):
        try:
            os.chown('test_file', '1000', '1000')
        except:
            self.fail('owner wasn\'t changed')

    def test_ch_permis(self):
        try:
            os.chmod('test_file', '777')
        except:
            self.fail('permissions wasn\'t changed')

