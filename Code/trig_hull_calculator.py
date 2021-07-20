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
	theta2 = math.atan((math.fabs((y2-y0)/(y2-y0))))
	if theta1 > theta2:
		hullX.append(pointsX[i+1])
		del pointsX[i]
		del pointsY[i]
	else:
		hullX.append(pointsX[i])
		del pointsX[i+1]
		del pointsY[i+1]

i = 1
while (i+1) != len(pointsX)-1:
	print(hullX)
	select_point(hullX[-1],pointsX[i],pointsX[i+1],hullY[-1], pointsY[i], pointsY[i+1])
	i+=1

