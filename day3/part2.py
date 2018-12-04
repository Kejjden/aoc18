import re
import itertools
def part2(claims):
	claim_lists = {}
	claim_length = {}
	for claim in claims:
		matches = re.search('#(?P<claim_id>\d+) @ (?P<left>\d+),(?P<top>\d+): (?P<width>\d+)x(?P<height>\d+)', claim)
		claim_lists[matches['claim_id']] = set(itertools.product(
			range(int(matches['top']), int(matches['top']) + int(matches['height'])), 
			range(int(matches['left']), int(matches['left']) + int(matches['width']))
		))
		claim_length[matches['claim_id']] = len(claim_lists[matches['claim_id']])

	for key, value in claim_lists.items():
		claim_set = value.copy()
		for inner_key, inner_value in claim_lists.items():
			if inner_key == key:
				continue
			claim_set -= inner_value
		if len(claim_set) == claim_length[key]:
			return key


if __name__ == '__main__':
	file = open("input", "r")
	claims = file.readlines()
	print(part2(claims))