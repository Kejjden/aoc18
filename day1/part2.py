from itertools import cycle

file = open("input", "r")
numbers = file.readlines()

freq = 0
seen = set()
for number in cycle(numbers):
	freq += int(number)
	if freq in seen:
		break
	seen.add(freq)

print(freq)