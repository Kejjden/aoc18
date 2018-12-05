import re
import operator
from collections import defaultdict
from datetime import datetime

def part2(notes):
	sorted_notes = sorted(notes)
	mins_asleep = defaultdict(int)
	sleep_minutes = defaultdict(lambda: defaultdict(int))

	current_guard = 0
	start_time = 0
	for note in sorted_notes:
		matches = re.search('#(?P<guard_id>\d+)', note)
		if matches is not None:
			current_guard = matches['guard_id']

		observed = note.rstrip()[19:]

		if observed == "falls asleep":
			start_time = note[15:17]
		if observed == "wakes up":
			end_time = note[15:17]
			mins_asleep[current_guard] += int(end_time) - int(start_time)
			for sleep_min in range(int(start_time), int(end_time)):
				sleep_minutes[current_guard][sleep_min] += 1

	maxed = 0
	maxed_guard = 0
	maxed_min = 0
	for guard in sleep_minutes:
		for minute in sleep_minutes[guard]:
			if sleep_minutes[guard][minute] > maxed:
				maxed = sleep_minutes[guard][minute]
				maxed_min = minute
				maxed_guard = guard


	return int(maxed_guard) * int(maxed_min)

if __name__ == '__main__':
	file = open('input', 'r')
	lines = file.readlines()
	print(part2(lines))

