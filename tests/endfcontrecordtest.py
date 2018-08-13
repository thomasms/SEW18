import unittest
import sewpy as sp


class ENDFContRecordUnitTest(unittest.TestCase):
    def setUp(self):
        self.record = sp.ENDFContRecord()

    def test_readLine(self):
        self.record.read(" 9.47990+08 9.46728+05          0          0          6          01809 8457    2")

        self.assertEqual(1809, self.record.MAT, "Assert MAT")
        self.assertEqual(8, self.record.MF, "Assert MF")
        self.assertEqual(457, self.record.MT, "Assert MT")
        self.assertEqual(2, self.record.NS, "Assert NS")
        self.assertEqual(9.47990e+08, self.record.C1, "Assert C1")
        self.assertEqual(9.46728e+05, self.record.C2, "Assert C2")
        self.assertEqual(0, self.record.L1, "Assert L1")
        self.assertEqual(0, self.record.L2, "Assert L2")
        self.assertEqual(6, self.record.N1, "Assert N1")
        self.assertEqual(0, self.record.N2, "Assert N2")
    
    def test_readLine2(self):
        self.record.read(" 0.0        0.0                 0          0          1        7105537 3  3    2")

        self.assertEqual(5537, self.record.MAT, "Assert MAT")
        self.assertEqual(3, self.record.MF, "Assert MF")
        self.assertEqual(3, self.record.MT, "Assert MT")
        self.assertEqual(2, self.record.NS, "Assert NS")
        self.assertEqual(0.0, self.record.C1, "Assert C1")
        self.assertEqual(0.0, self.record.C2, "Assert C2")
        self.assertEqual(0, self.record.L1, "Assert L1")
        self.assertEqual(0, self.record.L2, "Assert L2")
        self.assertEqual(1, self.record.N1, "Assert N1")
        self.assertEqual(710, self.record.N2, "Assert N2")
