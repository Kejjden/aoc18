# This works but is VEEEERRRY slow
# Check if it's faster to pre-compile a list of possible combinations, iterate and replace that

def part2(seq):
	chars = set(seq.lower())
	shortest = len(seq)

	for c in chars:
		new_len = run_for_char(c, seq)
		if new_len < shortest:
			shortest = new_len

	return shortest


def run_for_char(char, seq):
	print("Now removing", char)
	seq = seq.replace(char, '')
	seq = seq.replace(char.upper(), '')
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
	print(part2(lines))