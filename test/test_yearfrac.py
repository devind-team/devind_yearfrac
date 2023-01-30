import unittest
from yearfrac import yearfrac
from datetime import datetime
import numpy as np


class TestYearfrac(unittest.TestCase):
    def test1(self):
        d1 = datetime(2018, 12, 15)
        d2 = datetime(2019, 3, 1)
        x = yearfrac(d1, d2, 'act')
        self.assertEqual(round(x, 15), 0.208219178082192)

    def test2(self):
        d1 = datetime(2018, 12, 15)
        d2 = datetime(2019, 3, 1)
        x = yearfrac(d1, d2, 'act_isda')
        self.assertEqual(round(x, 8), round(0.208219178082118, 8))

    def test3(self):
        d1 = datetime(2018, 12, 15)
        d2 = datetime(2019, 3, 1)
        x = yearfrac(d1, d2, '30e360')
        self.assertEqual(round(x, 8), 0.21111111)

    def test4(self):
        d1 = datetime(2018, 12, 15)
        d2 = datetime(2019, 3, 1)
        x = yearfrac(d1, d2, '30e360_matu')
        self.assertEqual(round(x, 8), 0.21111111)

    def test_vector_vector(self):
        v1 = [datetime(2018, 12, 15), datetime(2018, 12, 15)]
        v2 = [datetime(2019, 3, 1), datetime(2019, 3, 1)]
        x = yearfrac(v1, v2, 'act')
        self.assertEqual(
            [round(x[0], 15), round(x[1], 15)],
            [0.208219178082192, 0.208219178082192]
        )

    def test_vector_scalar(self):
        v = [datetime(2018, 12, 15), datetime(2018, 12, 15)]
        s = datetime(2019, 3, 1)
        x = yearfrac(v, s, 'act')
        self.assertEqual(
            [round(x[0], 15), round(x[1], 15)],
            [0.208219178082192, 0.208219178082192]
        )

    def test_scalar_vector(self):
        s = datetime(2018, 12, 15)
        v = [datetime(2019, 3, 1), datetime(2019, 3, 1)]
        x = yearfrac(s, v, 'act')
        self.assertEqual(
            [round(x[0], 15), round(x[1], 15)],
            [0.208219178082192, 0.208219178082192]
        )

    def test_nparray_vector(self):
        v1 = np.array(
            [datetime(2018, 12, 15), datetime(2018, 12, 15)]
        )
        v2 = [datetime(2019, 3, 1), datetime(2019, 3, 1)]
        x = yearfrac(v1, v2, 'act')
        self.assertEqual(
            [round(x[0], 15), round(x[1], 15)],
            [0.208219178082192, 0.208219178082192]
        )


if __name__ == '__main__':
    unittest.main()
