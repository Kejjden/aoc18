file = open("input", "r")
numbers = file.readlines()

freq = 0

for number in numbers:
	freq += int(number)

print(freq)