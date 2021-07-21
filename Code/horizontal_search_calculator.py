import matplotlib.pyplot as plt
import math

pointsX = []
pointsY = []

for i in open("sample_data.csv","r").readlines():
	pointsX.append(int(i.split(",")[0]))
	pointsY.append(int(i.split(",")[1]))

hullX = [pointsX[0]] 
hullY = [pointsY[0]]

miny=min(pointsY)
print(miny)