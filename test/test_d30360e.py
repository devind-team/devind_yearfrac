import unittest
from yearfrac import d30360e


class Testd30360e(unittest.TestCase):
    def test1(self):
        x = d30360e(2018, 12, 15, 2019, 3, 1, False)
        self.assertEqual(round(x, 8), 0.21111111)

    def test2(self):
        x = d30360e(2018, 12, 15, 2019, 3, 1, True)
        self.assertEqual(round(x, 8), 0.21111111)


if __name__ == '__main__':
    unittest.main()
