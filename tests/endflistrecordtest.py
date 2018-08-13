import unittest
import sewpy as sp


class ENDFListRecordUnitTest(unittest.TestCase):
    def setUp(self):
        self.record = sp.ENDFListRecord()

    def test_readLine(self):
        lines = """ 3.50000+00 1.00000+00          0          0         12          21809 8457    4
 1.00000+00 0.00000+00 1.17563+06 1.70000+02 5.60055-02 0.00000+001809 8457    5
 1.00000+00 1.00000+00 5.13971+05 1.70000+02 9.43995-01 0.00000+001809 8457    6""".split('\n')
        self.record.read(lines)

        self.assertEqual(1809, self.record.listcont.MAT, "Assert MAT")
        self.assertEqual(8, self.record.listcont.MF, "Assert MF")
        self.assertEqual(457, self.record.listcont.MT, "Assert MT")
        self.assertEqual(4, self.record.listcont.NS, "Assert NS")
        self.assertEqual(4, self.record.listcont.NS, "Assert NS")
        self.assertEqual(3.5, self.record.listcont.C1, "Assert C1")
        self.assertEqual(1.0, self.record.listcont.C2, "Assert C2")
        self.assertEqual(0, self.record.listcont.L1, "Assert L1")
        self.assertEqual(0, self.record.listcont.L2, "Assert L2")
        self.assertEqual(12, self.record.listcont.N1, "Assert N1")
        self.assertEqual(2, self.record.listcont.N2, "Assert N2")

        # assert entries
        self.assertEqual(12, len(self.record), "Assert entries")
        self.assertEqual(1.0, self.record[0], "Assert first entry")
        self.assertEqual(0.0, self.record[1], "Assert second entry")
        self.assertEqual(1.17563e+06, self.record[2], "Assert third entry")
        self.assertEqual(1.7e+02, self.record[3], "Assert forth entry")
        self.assertEqual(5.60055e-02, self.record[4], "Assert fifth entry")
        self.assertEqual(0.0, self.record[5], "Assert sixth entry")
        self.assertEqual(1.0, self.record[6], "Assert seventh entry")
        self.assertEqual(1.0, self.record[7], "Assert eighth entry")
        self.assertEqual(5.13971e+05, self.record[8], "Assert ninth entry")
        self.assertEqual(1.7e+02, self.record[9], "Assert tenth entry")
        self.assertEqual(9.43995e-01, self.record[10], "Assert eleventh entry")
        self.assertEqual(0.0, self.record[11], "Assert twelveth entry")

