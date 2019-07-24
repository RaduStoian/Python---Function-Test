import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_equals(self):
        self.assertEqual(calc.nextNumber('123'), '132')
        self.assertEqual(calc.nextNumber(123), '132')
        self.assertEqual(calc.nextNumber('0200'), '1001')
        self.assertEqual(calc.nextNumber('09999999999999'), '18999999999999')
        self.assertEqual(calc.nextNumber('90'), '-1')
        self.assertEqual(calc.nextNumber('9999'), '-1')
        self.assertEqual(calc.nextNumber('01000000000'), '10000000000')
        self.assertEqual(calc.nextNumber('-10'), '-1')
        self.assertEqual(calc.nextNumber('"ds'), '-1')
        

if __name__ == '__main__':
    unittest.main()        