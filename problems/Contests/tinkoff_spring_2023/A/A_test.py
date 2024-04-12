import unittest

from problems.Contests.tinkoff_spring_2023.A.A import solve


class MyTestCase(unittest.TestCase):
    def test_A(self):
        a = 9
        b = [5, 5, 4, 5, 4, 5, 4, 5, 4]
        want = 4
        self.assertEqual(solve(b), want)

    def test_A2(self):
            a = 8
            b = [3, 4, 4, 4, 4, 5, 4, 5]
            want = 2
            self.assertEqual(solve(b), want)

    def test_A3(self):
            a = 10
            b = [5, 5, 5, 5, 5, 3, 5, 5, 5, 5]
            want = -1
            self.assertEqual(solve(b), want)



if __name__ == '__main__':
    unittest.main()
