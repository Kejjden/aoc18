def part2(ids):
	match_count = len(ids[0]) - 1
	for box_id in ids:
		for compare_to in ids:
			matches = [i for i, j in zip(box_id, compare_to) if i == j]
			if len(matches) == match_count:
				return "".join(matches)

if __name__ == '__main__':
	file = open("input", "r")
	ids = file.readlines()
	print(part2(ids))