import unittest
from part1 import part1
from part2 import part2

class TestPart1(unittest.TestCase):
	def test_part1(self):
		seq = [
			"1, 1",
			"1, 6",
			"8, 3",
			"3, 4",
			"5, 5",
			"8, 9"
		]
		self.assertEqual(part1(seq), 17)

class TestPart2(unittest.TestCase):
	def test_part2(self):
		seq = "dabAcCaCBAcCcaDA"
		self.assertEqual(part2(seq), 4)

if __name__ == '__main__':
	unittest.main()

