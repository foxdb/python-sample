# -*- coding: utf-8 -*-

import unittest

from .context import sample


class BasicTestSuite(unittest.TestCase):
    """Unit tests"""

    def test_true_is_true(self):
        assert True

    def test_divide_none_for_0(self):
        self.assertIsNone(sample.core.divide(1, 0))

    def test_divide_result(self):
        self.assertEqual(sample.core.divide(10, 5), 2)

    def test_modulo_none_when_0(self):
        self.assertIsNone(sample.core.modulo(1, 0))

    def test_modulo_positive_0(self):
        self.assertEqual(sample.core.modulo(10, 5), 0)

    def test_modulo_positive_1(self):
        self.assertEqual(sample.core.modulo(10, 3), 1)


if __name__ == '__main__':
    unittest.main()
