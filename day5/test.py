import unittest
from part1 import part1
from part2 import part2

class TestPart1(unittest.TestCase):
	def test_part1(self):
		seq = "dabAcCaCBAcCcaDA"
		self.assertEqual(part1(seq), 10)

class TestPart2(unittest.TestCase):
	def test_part2(self):
		seq = "dabAcCaCBAcCcaDA"
		self.assertEqual(part2(seq), 4)

if __name__ == '__main__':
	unittest.main()

