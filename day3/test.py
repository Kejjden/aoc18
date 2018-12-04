import unittest
from part1 import part1
from part2 import part2

class TestPart1(unittest.TestCase):
	def test_part1(self):
		claims = [
			"#1 @ 1,3: 4x4",
			"#2 @ 3,1: 4x4",
			"#3 @ 5,5: 2x2"
		]
		self.assertEqual(part1(claims), 4)

class TestPart2(unittest.TestCase):
	def test_part2(self):
		claims = [
			"#1 @ 1,3: 4x4",
			"#2 @ 3,1: 4x4",
			"#3 @ 5,5: 2x2"
		]
		self.assertEqual(part2(claims), "3")

if __name__ == '__main__':
	unittest.main()

