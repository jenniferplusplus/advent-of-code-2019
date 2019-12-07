import unittest
from day_04.lib import valid_pairs, valid_sequence

class MyTestCase(unittest.TestCase):
    def test_sequence(self):
        self.assertTrue(valid_sequence(123456))
        self.assertTrue(valid_sequence(234567))
        self.assertTrue(valid_sequence(345678))
        self.assertFalse(valid_sequence(567890))
        self.assertFalse(valid_sequence(111110))

    def test_pairs(self):
        self.assertTrue(valid_pairs(112345))
        self.assertTrue(valid_pairs(111345))
        self.assertTrue(valid_pairs(111145))
        self.assertTrue(valid_pairs(456678))
        self.assertTrue(valid_pairs(456688))
        self.assertFalse(valid_pairs(123456))

if __name__ == '__main__':
    unittest.main()
