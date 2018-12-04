from itertools import cycle

def part2(numbers):
	freq = 0
	seen = set()
	for number in cycle(numbers):
		freq += int(number)
		if freq in seen:
			break
		seen.add(freq)

	return freq

if __name__ == '__main__':
	file = open("input", "r")
	numbers = file.readlines()
	print(part2(numbers))