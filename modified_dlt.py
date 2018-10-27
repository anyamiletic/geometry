import dlt
import numpy as np

def sqrt(number):
	return number**(1/2.0)

def get_focus_point(points):
	focus_point = [0.0,0.0]
	brojac = 0

	for point in points:
		focus_point[0] += point[0]
		focus_point[1] += point[1]
		brojac += 1

	focus_point[0] /= brojac
	focus_point[1] /= brojac

	return focus_point

def get_average_dist(points):
	av_dist = 0
	for point in points:
		av_dist += np.linalg.norm(point)

	return av_dist

def get_2d_coords(points_arg):
	points = []

	for point in points_arg:
		point_x = point[0]/point[2]
		point_y = point[1]/point[2]
		points.append([point_x, point_y])

	return points

def get_t(points):

	fx, fy = get_focus_point(points)

	#translate to 0,0,0
	tx = -1*fx
	ty = -1*fy

	G = np.array([
		[1,0,tx],
		[0,1,ty],
		[0,0,1]
		])

	#scale
	dist = get_average_dist(points)
	S = np.array([
		[sqrt(2)/dist,   0,      0],
		[0,         sqrt(2)/dist,0],
		[0,            0,      1]
		])

	T = np.dot(S,G)
	return T

def func(original, images):

	points_original = get_2d_coords(original)
	points_images  = get_2d_coords(images)
	#print("points original")
	#print(points_original)

	T = get_t(points_original)
	Tp = get_t(points_images)
	#print("matrica transformacija t")
	#print(T)
	#print("matrica transformacija tp")
	#print(Tp)

	points_o = []
	points_i = []

	for point in original:
		points_o.append(np.dot(T, point))
	for point in images:
		points_i.append(np.dot(Tp, point))

	#print("points_o:")
	#print(points_o)
	P = dlt.dlt(points_o, points_i)

	P_final = np.dot(np.linalg.inv(T), P).dot(T)

	return P_final


