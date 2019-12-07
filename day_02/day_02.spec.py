import unittest
from day_02.lib import IntCodeProcessor

test_data = {
    'add': [1, 0, 0, 5, 99, 0, 0, 0],
    'multiply': [2, 0, 6, 5, 99, 0, 4, 0],
    'all': [1, 0, 2, 0, 2, 0, 4, 9, 99, 0, 0, 0]
}

class MyTestCase(unittest.TestCase):
    @unittest.skip('dev')
    def test_get_next(self):
        icp = IntCodeProcessor(test_data.get('add'))
        expected = [1, 0, 0, 3]
        self.assertSequenceEqual(icp.next_code_block(), expected)
        return

    @unittest.skip('dev')
    def test_op_add(self):
        icp = IntCodeProcessor(test_data.get('add'))
        block = icp.next_code_block()
        icp.process_code_block(block)

        expected = 2
        self.assertEqual(icp.int_code[5], expected)

    @unittest.skip('dev')
    def test_op_mult(self):
        icp = IntCodeProcessor(test_data.get('multiply'))
        block = icp.next_code_block()
        icp.process_code_block(block)

        expected = 8
        self.assertEqual(icp.int_code[5], expected)

    def test_all(self):
        icp = IntCodeProcessor(test_data.get('all'))
        icp.process_int_code()

        expected = [3, 0, 2, 0, 2, 0, 4, 9, 99, 6, 0, 0]
        self.assertSequenceEqual(icp.int_code, expected)

if __name__ == '__main__':
    unittest.main()
