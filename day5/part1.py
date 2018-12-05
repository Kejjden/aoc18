def part1(seq):
	while True:
		new_seq = react(seq)
		if new_seq is None:
			return len(seq)
		seq = new_seq

def react(seq):
	for i in range(0, len(seq)-1):
		a, b = seq[i:i+2]
		if not a == b and a.lower() == b.lower():
			return seq[:i]+seq[i+2:]
	return None

if __name__ == '__main__':
	file = open('input', 'r')
	lines = file.read()
	print(part1(lines))

