import unittest

from tests.numericaltest import NumericalUnitTest 


def main():
    unittest.TextTestRunner(verbosity=3).run(unittest.TestSuite())

if __name__ == '__main__':
    unittest.main()
