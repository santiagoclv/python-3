""" 
    Writing test cases are very important to know if a piace of code do what it needs to do even in the border and more extrange cases.

        assertEqual(a, b)               a == b
        assertNotEqual(a, b)            a != b
        assertTrue(x)                   bool(x) is True
        assertFalse(x)                  bool(x) is False
        assertIs(a, b)                  a is b
        assertIsNot(a, b)               a is not b
        assertIsNone(x)                 x is None
        assertIsNotNone(x)              x is not None
        assertIn(a, b)                  a in b
        assertNotIn(a, b)               a not in b
        assertIsInstance(a, b)          isinstance(a, b)
        assertNotIsInstance(a, b)       not isinstance(a, b)
"""

import unittest
from message import Message

class TestStringMethods(unittest.TestCase):
    """ The three individual tests are defined with methods whose names start with the letters test.
        This naming convention informs the test runner about which methods represent tests."""

    def setUp(self):
        self.message = Message('hello world')

    # def tearDown(self):
        # Here we could be the place to clean up everything from the test
        #  self.message.dispose()

    def test_upper(self):
        self.assertEqual(self.message.body.upper(), 'HELLO WORLD')

    def test_isupper(self):
        self.assertTrue('HELLO WORLD'.isupper())
        self.assertFalse(self.message.body.isupper())

    def test_split(self):
        self.assertEqual(self.message.body.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            self.message.body.split(2)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods('test_upper'))
    suite.addTest(TestStringMethods('test_isupper'))
    suite.addTest(TestStringMethods('test_split'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())