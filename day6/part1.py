import string
import math
from collections import OrderedDict, defaultdict

def check_points(seq, overflow):
	points = dict(zip([str(i) for i in range(0, len(seq))], [dict(
		zip(
			['x', 'y', 'size'], 
			([int(i) for i in x.split(', ')] + [0])
		)
	) for x in seq]))

	hull_min_y = points[min(points, key=lambda i: points[i]['y'])]["y"]
	hull_max_y = points[max(points, key=lambda i: points[i]['y'])]["y"]
	hull_min_x = points[min(points, key=lambda i: points[i]['x'])]["x"]
	hull_max_x = points[max(points, key=lambda i: points[i]['x'])]["x"]
	
	for grid_y in range(hull_min_y-overflow, hull_max_y+overflow):
		for grid_x in range(hull_min_x-overflow, hull_max_x+overflow):

			shortest_distance = 9999999
			shortest_distance_point_index = []

			for point_index in points:
				dist = abs(points[point_index]['y'] - grid_y) + abs(points[point_index]['x'] - grid_x)
				if dist < shortest_distance:
					shortest_distance = dist
					shortest_distance_point_index = [point_index]
				elif dist is shortest_distance:
					shortest_distance_point_index.append(point_index)

			if len(shortest_distance_point_index) == 1:
				points[shortest_distance_point_index[0]]['size'] += 1

	return points

def part1(seq):
	points = check_points(seq, 0)
	points2 = check_points(seq, 20)
	
	max_zone = 0
	for pi in points:
		if points[pi]['size'] == points2[pi]['size'] and points[pi]['size'] > max_zone:
			max_zone = points[pi]["size"]
	
	return max_zone



if __name__ == '__main__':
	file = open('input', 'r')
	lines = file.readlines()
	print(part1(lines))

