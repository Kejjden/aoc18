import re
from collections import defaultdict

def part1(claims):
	fabric = set()
	overlaps = set()
	overlap_counter = 0
	for claim in claims:
		matches = re.search('@ (?P<left>\d+),(?P<top>\d+): (?P<width>\d+)x(?P<height>\d+)', claim)
		for h in range(int(matches['top']), int(matches['top']) + int(matches['height'])):
			for w in range(int(matches['left']), int(matches['left']) + int(matches['width'])):
				key = str(h) + "x" + str(w)
				if key in fabric:
					if key not in overlaps:
						overlaps.add(key)
				fabric.add(key)
	return len(overlaps)

if __name__ == '__main__':
	file = open("input", "r")
	ids = file.readlines()
	print(part1(ids))

