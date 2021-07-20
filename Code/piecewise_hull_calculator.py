'''
Certain points in the function will not be included in the hull.
These are the points that have a greater gradient going into them
than coming out.
'''

import matplotlib.pyplot as plt

#Create arrays to store the functions
pointsX = []
pointsY = []
grads = []


#Load in functions as points
for i in open("sample_data.csv","r").readlines():
	pointsX.append(int(i.split(",")[0]))
	pointsY.append(int(i.split(",")[1]))

hullX = [pointsX[0]] 
hullY = [pointsY[0]]

#Get gradients between points
def grad(x0,x1,y0,y1):
	return (y1-y0)/(x1-x0)

#Calculate gradients of each part of the function
for i in range(0, len(pointsX)-1):
	m = grad(pointsX[i],pointsX[i+1], pointsY[i], pointsY[i+1])
	grads.append(m)

#Create the hull
for i in range(1, len(pointsX)-1):
	if grads[i-1] < grads[i]:
		hullX.append(pointsX[i])
		hullY.append(pointsY[i])

hullX.append(pointsX[len(pointsX)-1])
hullY.append(pointsY[len(pointsY)-1])

def plot_hull(pointsX, pointsY, hullX, hullY):
	plt.plot(pointsX,pointsY, 'b', label="f(x)")
	plt.plot(hullX, hullY, '--r', label="CHull(f(x))")
	plt.legend(loc="upper left")
	plt.show()

plot_hull(pointsX,pointsY,hullX,hullY)