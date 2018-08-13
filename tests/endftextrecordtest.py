import unittest
import sewpy as sp


class ENDFTextRecordUnitTest(unittest.TestCase):
    def setUp(self):
        self.record = sp.ENDFTextRecord()

    def test_readLine(self):
        self.record.read("         Ex = 0.0         keV                     1 decay mode(s) 1809 1451   21")

        self.assertEqual(1809, self.record.MAT, "Assert MAT")
        self.assertEqual(1, self.record.MF, "Assert MF")
        self.assertEqual(451, self.record.MT, "Assert MT")
        self.assertEqual(21, self.record.NS, "Assert NS")
        self.assertEqual("         Ex = 0.0         keV                     1 decay mode(s) ", self.record.text, "Assert text")
    
    def test_readLine2(self):
        self.record.read(" 1.87871+05 9.04425+02 1.64430+00 2.26801-01 0.00000+00 0.00000+001809 8457    3")

        self.assertEqual(1809, self.record.MAT, "Assert MAT")
        self.assertEqual(8, self.record.MF, "Assert MF")
        self.assertEqual(457, self.record.MT, "Assert MT")
        self.assertEqual(3, self.record.NS, "Assert NS")
        self.assertEqual(" 1.87871+05 9.04425+02 1.64430+00 2.26801-01 0.00000+00 0.00000+00", self.record.text, "Assert text")
