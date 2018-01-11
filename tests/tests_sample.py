
# -*- coding: utf-8 -*-

from .context import sample

import unittest

class BasicTestSuite(unittest.TestCase):
    """Sample tests"""

    def test_if_true_is_true(self):
        assert True

    def test_thoughts(self):
        self.assertIsNone(sample.hmm())

if __name__ == '__main__':
    unittest.main()