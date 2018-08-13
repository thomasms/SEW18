import unittest
import sewpy as sp


class ENDFRecordUnitTest(unittest.TestCase):
    def setUp(self):
        self.record = sp.ENDFRecord()
    
    def test_readLine(self):
        self.record.read("137CS B- DECAY              Q =  1175.6300 keV       0.1700       1809 1451   23")

        self.assertEqual(1809, self.record.MAT, "Assert MAT")
        self.assertEqual(1, self.record.MF, "Assert MF")
        self.assertEqual(451, self.record.MT, "Assert MT")
        self.assertEqual(23, self.record.NS, "Assert NS")
    
    def test_readLine2(self):
        self.record.read(" 1.87871+05 9.04425+02 1.64430+00 2.26801-01 0.00000+00 0.00000+001809 8457    3")

        self.assertEqual(1809, self.record.MAT, "Assert MAT")
        self.assertEqual(8, self.record.MF, "Assert MF")
        self.assertEqual(457, self.record.MT, "Assert MT")
        self.assertEqual(3, self.record.NS, "Assert NS")


