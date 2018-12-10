import string
import math
from collections import OrderedDict, defaultdict

def part1(seq):
	og_points = dict(zip(string.ascii_uppercase, [dict(zip(['x', 'y'], [int(i) for i in x.split(', ')])) for x in seq]))
	closest = defaultdict(int)
	points = og_points.copy()
	hull = quick_hull(points)

	hull_min_y = hull[min(hull, key=lambda i: hull[i]['y'])]
	hull_max_y = hull[max(hull, key=lambda i: hull[i]['y'])]
	hull_min_x = hull[min(hull, key=lambda i: hull[i]['x'])]
	hull_max_x = hull[max(hull, key=lambda i: hull[i]['x'])]
	
	boundry_box = {
		'tl': {'x': hull_min_x['x'], 'y': hull_min_y['y']},  # top left
		'tr': {'x': hull_max_x['x'], 'y': hull_min_y['y']},  # top right
		'br': {'x': hull_min_x['x'], 'y': hull_max_y['y']},  # bottom right
		'bl': {'x': hull_max_x['x'], 'y': hull_max_y['y']}   # bottom left
	}

	for grid_y in range(hull_min_y['y'], hull_max_y['y']):
		for grid_x in range(hull_min_x['x'], hull_max_x['x']):

			shortest_distance = 99999
			shortest_distance_point_index = []

			for point_index in og_points:
				dist = math.sqrt( (og_points[point_index]['x'] - grid_x)**2 + (og_points[point_index]['y'] - grid_y)**2 )

				if dist < shortest_distance:
					shortest_distance = dist
					shortest_distance_point_index = [point_index]
				elif dist is shortest_distance:
					shortest_distance_point_index.append(point_index)

			if len(shortest_distance_point_index) == 1:
				closest[shortest_distance_point_index[0]] += 1


	maxman = max([x for x in closest if x not in hull.keys()], key=lambda i: closest[i])

	return closest[maxman] + 1

def quick_hull(points):
	hull = {}

	max_x = max(points, key=lambda i: points[i]['x'])
	min_x = min(points, key=lambda i: points[i]['x'])

	hull[max_x] = points.pop(max_x)
	hull[min_x] = points.pop(min_x)

	right_of_line = {}
	left_of_line = {}

	for point in points:
		side = (hull[min_x]['x']-hull[max_x]['x'])*(points[point]['y']-hull[max_x]['y'])-(points[point]['x']-hull[max_x]['x'])*(hull[min_x]['y']-hull[max_x]['y'])
		if side > 0:
			left_of_line[point] = points[point]
		if side < 0:
			right_of_line[point] = points[point]

	quick_hull_find(right_of_line, max_x, min_x, hull)
	quick_hull_find(left_of_line, min_x, max_x, hull)

	return hull

def quick_hull_find(sk, p, q, hull):
	if len(sk) == 0:
		return

	p_point = hull[p]
	q_point = hull[q]

	farthest_point = max(sk, key=lambda point: math.sqrt(((q_point['y']-p_point['y'])*(sk[point]['x']-p_point['x'])+(q_point['x']-p_point['x'])*(sk[point]['y']-p_point['y']))**2/((q_point['x']-p_point['x'])**2 + (q_point['y']-p_point['y'])**2)))

	hull[farthest_point] = sk.pop(farthest_point)
	c_point = hull[farthest_point]
	s1 = {}
	s2 = {}

	for point in sk:
		pc_side = (c_point['x']-p_point['x'])*(sk[point]['y']-p_point['y'])-(sk[point]['x']-p_point['x'])*(c_point['y']-p_point['y'])
		cq_side = (q_point['x']-c_point['x'])*(sk[point]['y']-c_point['y'])-(sk[point]['x']-c_point['x'])*(q_point['y']-c_point['y'])
		if pc_side < 0:
			s1[point] = sk[point]
		if cq_side < 0:
			s2[point] = sk[point]

	quick_hull_find(s1, p, farthest_point, hull)
	quick_hull_find(s2, farthest_point, q, hull)


if __name__ == '__main__':
	file = open('input', 'r')
	lines = file.readlines()
	print(part1(lines))

