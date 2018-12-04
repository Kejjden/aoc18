import unittest
from part1 import part1
from part2 import part2

class TestPart1(unittest.TestCase):
	def test_part1(self):
		ids = [
			"abcdef", 
			"bababc", 
			"abbcde", 
			"abcccd", 
			"aabcdd", 
			"abcdee", 
			"ababab"
		]
		self.assertEqual(part1(ids), 12)

class TestPart2(unittest.TestCase):
	def test_part2(self):
		ids = [
			"abcde", 
			"fghij", 
			"klmno", 
			"pqrst", 
			"fguij", 
			"axcye", 
			"wvxyz"
		]
		self.assertEqual(part2(ids), "fgij")

if __name__ == '__main__':
	unittest.main()

