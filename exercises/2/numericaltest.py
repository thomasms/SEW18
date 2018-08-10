import unittest
import math
from numerical import isfloat, getfloat


class NumericalUnitTest(unittest.TestCase):

    def test_isfloat(self):
        self.assertEqual(isfloat(""), False)
        self.assertEqual(isfloat("-0.000E+00"), True)
        self.assertEqual(isfloat("1234567"), True)
        self.assertEqual(isfloat("NaN"), True)
        self.assertEqual(isfloat("NaNananana BATMAN"), False)
        self.assertEqual(isfloat("123.456"), True)
        self.assertEqual(isfloat("123.E4"), True)
        self.assertEqual(isfloat(".1"), True)
        self.assertEqual(isfloat("1,234"), False)
        self.assertEqual(isfloat("NULL"), False)
        self.assertEqual(isfloat(",1"), False)
        self.assertEqual(isfloat("123.EE4"), False)
        self.assertEqual(isfloat("6.523537535629999e-07"), True)
        self.assertEqual(isfloat("6e777777"), True)
        self.assertEqual(isfloat("iNF"), True)
        self.assertEqual(isfloat("-iNF"), True)
        self.assertEqual(isfloat("infinity"), True)
        self.assertEqual(isfloat("1.797693e+308"), True)
        self.assertEqual(isfloat("2.65773-317"), True)
        self.assertEqual(isfloat("-3.83922-308"), True)
        self.assertEqual(isfloat("-4.10537-305"), True)
        self.assertEqual(isfloat("1.0+9"), True)
        self.assertEqual(isfloat("1.0+1.0"), False)
        self.assertEqual(isfloat("1+1.0"), False)
        self.assertEqual(isfloat("1+1"), False)
        self.assertEqual(isfloat("1-1"), False)
        self.assertEqual(isfloat("2.65773-+317"), False)
        self.assertEqual(isfloat("2f-317"), False)
        self.assertEqual(isfloat("2f-3d"), False)
        self.assertEqual(isfloat("2-2+3d"), False)
        self.assertEqual(isfloat("12.34.56"), False)
        self.assertEqual(isfloat("#56"), False)
        self.assertEqual(isfloat("56f"), False)
        self.assertEqual(isfloat("56.4d"), False)
        self.assertEqual(isfloat("56%"), False)
        self.assertEqual(isfloat("0E0"), True)
        self.assertEqual(isfloat("x86E0"), False)
        self.assertEqual(isfloat(True), True)
        self.assertEqual(isfloat("True"), False)
        self.assertEqual(isfloat("86-5"), False)
        self.assertEqual(isfloat("+1e1^5"), False)
        self.assertEqual(isfloat("+1e1"), True)
        self.assertEqual(isfloat("-+1"), False)
        self.assertEqual(isfloat("-+"), False)
        self.assertEqual(isfloat("+"), False)
        self.assertEqual(isfloat("-"), False)
        self.assertEqual(isfloat("0-0"), False)
        self.assertEqual(isfloat("0.0-0"), True)
        self.assertEqual(isfloat("(1)"), False)
        self.assertEqual(isfloat(None), False)

    def test_getfloat(self):
        self.assertEqual(getfloat("1234567"), 1234567)
        self.assertEqual(math.isnan(getfloat("NaN")), True)
        self.assertEqual(getfloat("123.456"), 123.456)
        self.assertEqual(getfloat("123.E4"), 123.E4)
        self.assertEqual(getfloat(".1"), 0.1)
        self.assertEqual(getfloat("6.523537535629999e-07"), 6.523537535629999e-07)
        self.assertEqual(getfloat("6e777777"), 6e777777)
        self.assertEqual(math.isinf(getfloat("iNF")), True)
        self.assertEqual(math.isinf(getfloat("-iNF")), True)
        self.assertEqual(math.isinf(getfloat("infinity")), True)
        self.assertEqual(getfloat("1.797693e+308"), 1.797693e+308)
        self.assertEqual(getfloat("2.65773-317"), 2.65773e-317)
        self.assertEqual(getfloat("2.65773+317"), 2.65773e+317)
        self.assertEqual(getfloat("2.65773-300"), 2.65773e-300)
        self.assertEqual(getfloat("2.65773-31"), 2.65773e-31)
        self.assertEqual(getfloat("-3.83922-308"), -3.83922e-308)
        self.assertEqual(getfloat("-4.10537-305"), -4.10537e-305)
        self.assertEqual(getfloat("1.0+9"), 1.0e+9)
        self.assertEqual(getfloat("0E0"), 0.0)
        self.assertEqual(getfloat("0.0-0"), 0.0)
        self.assertEqual(getfloat("-0.000E+00"), 0.0)
        self.assertEqual(getfloat("+1e1"), 10)
        self.assertEqual(getfloat("-1e1"), -10)
        self.assertEqual(getfloat("-1.1e1"), -11)
        self.assertEqual(getfloat("+"), "nan")
        self.assertEqual(getfloat("-"), "nan")

