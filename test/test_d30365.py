import unittest
from yearfrac import d30365


class TestActIsda(unittest.TestCase):
    def test1(self):
        x = d30365(2018, 12, 15, 2019, 3, 1)
        self.assertEqual(round(x, 8), 0.20821918)


if __name__ == '__main__':
    unittest.main()
