from unittest import TestCase
from main import Solution


class TestSolution(TestCase):
	def test_decode1(self):
		s = "abc"
		t = "ahbgdc"
		sol = Solution()
		got = sol.isSubsequence(s, t)
		want = True
		self.assertEqual(want, got)

	def test_encode1(self):
		s = "axc"
		t = "ahbgdc"
		sol = Solution()
		got = sol.isSubsequence(s, t)
		want = False
		self.assertEqual(want, got)
