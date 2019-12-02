import unittest
from day_01.lib import fuel_calc


class MyTestCase(unittest.TestCase):
    # @unittest.skip('')
    def test_12(self):
        self.assertEqual(fuel_calc(12), 2)

    # @unittest.skip('')
    def test_14(self):
        self.assertEqual(fuel_calc(14), 2)

    # @unittest.skip('')
    def test_1969(self):
        self.assertEqual(fuel_calc(1969), 966)

    # @unittest.skip()
    def test_100756(self):
        self.assertEqual(fuel_calc(100756), 50346)

if __name__ == '__main__':
    unittest.main()
