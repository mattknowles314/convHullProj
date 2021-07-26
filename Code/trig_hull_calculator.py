import matplotlib.pyplot as plt
import math

#Create arrays to store the functions
pointsX = []
pointsY = []

#Load in functions as points
for i in open("sample_data.csv","r").readlines():
	pointsX.append(int(i.split(",")[0]))
	pointsY.append(int(i.split(",")[1]))

hullX = [pointsX[0]] 
hullY = [pointsY[0]]

def select_point(x0,x1,x2,y0,y1,y2):
	theta1 = math.atan((math.fabs((y1-y0)/(x1-x0))))
	theta2 = math.atan((math.fabs((y2-y0)/(x2-x0))))
	if theta1 > theta2:
		hullX.append(pointsX[i+1])
		hullY.append(pointsY[i+1])
	else:
		hullX.append(pointsX[i])
		hullY.append(pointsY[i])

i = 0
while (i+1) != len(pointsX)-1:
	print(hullX)
	select_point(hullX[i-1],pointsX[i],pointsX[i+1],hullY[i-1], pointsY[i], pointsY[i+1])
	i+=1