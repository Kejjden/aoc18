import collections

def part1(ids):
	exactly_2 = 0
	exactly_3 = 0

	for box_id in ids:
		occurances = collections.Counter(box_id).values()
		if 2 in occurances:
			exactly_2 += 1
		if 3 in occurances:
			exactly_3 += 1

	return exactly_2 * exactly_3

if __name__ == '__main__':
	file = open("input", "r")
	ids = file.readlines()
	print(part1(ids))

