def part1(numbers):
	freq = 0

	for number in numbers:
		freq += int(number)

	return freq

if __name__ == '__main__':
	file = open("input", "r")
	numbers = file.readlines()
	print(part1(numbers))

