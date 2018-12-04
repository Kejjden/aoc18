import unittest
from part1 import part1
from part2 import part2

class TestPart1(unittest.TestCase):
	def test_part1(self):
		ids = ["+1", "-2", "+3", "+1"]
		self.assertEqual(part1(numbers), 3)

class TestPart2(unittest.TestCase):
	def test_part2(self):
		numbers = ["+3", "+3", "+4", "-2", "-4"]
		self.assertEqual(part2(numbers), 10)

if __name__ == '__main__':
	unittest.main()

