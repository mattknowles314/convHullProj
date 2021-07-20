'''
Certain points in the function will not be included in the hull.
These are the points that have a greater gradient going into them
than coming out.
'''

import matplotlib.pyplot as plt

#Load in functions as points
pointsX = []
pointsY = []
for i in open("sample_data2.csv","r").readlines():
	pointsX.append(int(i.split(",")[0]))
	pointsY.append(int(i.split(",")[1]))


#Get gradients between points
def grad(x0,x1,y0,y1):
	return (y1-y0)/(x1-x0)

grads = []
for i in range(0, len(pointsX)-1):
	m = grad(pointsX[i],pointsX[i+1], pointsY[i], pointsY[i+1])
	grads.append(m)

#Create the hull
hullX = [pointsX[0]] 
hullY = [pointsY[0]]
for i in range(1, len(pointsX)-1):
	if grads[i-1] < grads[i]:
		hullX.append(pointsX[i])
		hullY.append(pointsY[i])
hullX.append(pointsX[len(pointsX)-1])
hullY.append(pointsY[len(pointsY)-1])

plt.plot(pointsX,pointsY, 'b', hullX, hullY, '--r')
plt.show()