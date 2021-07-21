'''
Certain points in the function will not be included in the hull.
These are the points that have a greater gradient going into them
than coming out.
'''

import matplotlib.pyplot as plt
import math

#Create arrays to store the functions
pointsX = []
pointsY = []
grads = []
hullGrads = []

#Load in functions as points
for i in open("sample_data.csv","r").readlines():
	pointsX.append(int(i.split(",")[0]))
	pointsY.append(int(i.split(",")[1]))

hullX = [pointsX[0]] 
hullY = [pointsY[0]]

def plot_hull(pointsX, pointsY, hullX, hullY):
	plt.plot(pointsX,pointsY, 'b', label="f(x)")
	plt.plot(hullX, hullY, '--r', label="CHull(f(x))")
	plt.legend(loc="upper left")
	plt.show()

#Get gradients between points
def grad(x0,x1,y0,y1):
	return (y1-y0)/(x1-x0)

#Calculate gradients of each part of the function
def grad_dif(x0,y0, gradArray):
	for i in range(0, len(x0)-1):
		gradArray.append(grad(x0[i],x0[i+1], y0[i], y0[i+1]))

grad_dif(pointsX,pointsY, grads)

for i in range(1, len(pointsX)-1):
	if grads[i-1] < grads[i]:
		hullX.append(pointsX[i])
		hullY.append(pointsY[i])

hullX.append(pointsX[-1])
hullY.append(pointsY[-1])

grad_dif(hullX, hullY, hullGrads)

t = len(hullGrads)-1
q = 1
while q <= t:
	if hullGrads[q-1] > hullGrads[q]:
		del hullX[q]
		del hullY[q]
		hullGrads = []
		grad_dif(hullX, hullY, hullGrads)
		t-=1
	else:
		q+=1


#plot_hull(pointsX,pointsY,hullX,hullY)