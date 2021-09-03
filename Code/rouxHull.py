import matplotlib.pyplot as plt
import time
import random
import statistics as st

def grad(x0,x1,y0,y1):
	return (y1-y0)/(x1-x0)

def roux_conv_hull(S):
	'''
	INPUT: S, a 2D array of coordinates for the hull to be calculated on.
	OUTPUT: A 2D array of coordinates representing the convex hull of S
	'''
	hull = [S[0]]
	curr_point = 0
	while S[-1] not in hull:
		grads = []
		for i in range(curr_point, len(S)-1):
			grads.append(grad(S[curr_point][0],S[i+1][0],S[curr_point][1],S[i+1][1]))
		m = grads.index(min(grads))
		hull.append(S[curr_point+1+m])
		curr_point = curr_point+1+m
	return hull