#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_plushcap
----------------------------------

Tests for `plushcap` module.
"""
import sys
import os

import unittest

sys.path.append(os.path.join('..', 'plushcap'))
from plushcap import plushcap


class TestPlushcap(unittest.TestCase):
    """
        Tests that URLs can be retrieved when they exist. URLs that do not
        exist or are down return the proper status codes.
    """
    def setUp(self):
        self.working_url = "http://www.fullstackpython.com/"
        self.non_existent_url = "http://localhost:8889/"
    
    def tearDown(self):
        pass

    def test_working_url(self):
        status_code, content = plushcap.contact_url(self.working_url)
        self.assertEqual(status_code, 200)

    def test_non_existent_url(self):
        status_code, content = plushcap.contact_url(self.non_existent_url)
        self.assertEqual(status_code, plushcap.CONNECTION_ERROR)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPlushcap)
    unittest.TextTestRunner().run(suite)
