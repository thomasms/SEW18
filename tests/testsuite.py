import unittest

from tests.numericaltest import NumericalUnitTest
from tests.endfrecordtest import ENDFRecordUnitTest
from tests.endfcontrecordtest import ENDFContRecordUnitTest
from tests.endfheadrecordtest import ENDFHeadRecordUnitTest
from tests.endflistrecordtest import ENDFListRecordUnitTest
from tests.endftextrecordtest import ENDFTextRecordUnitTest


def main():
    unittest.TextTestRunner(verbosity=3).run(unittest.TestSuite())

if __name__ == '__main__':
    unittest.main()
