#!/usr/bin/env python3

import unittest
import os.path

class TestFile(unittest.TestCase):
    """
    Test class
    """

    def test_file_exist(self):
        """
        Test if file exist
        """
        self.assertTrue(os.path.exists('/tmp/dgplug.txt'))


if __name__ == '__main__':
    unittest.main()        



