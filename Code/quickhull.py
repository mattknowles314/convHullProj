import matplotlib.pyplot as plt
pointsX = []
pointsY = []

def grad(x0,x1,y0,y1):
	return (y1-y0)/(x1-x0)

#Load in functions as points
for i in open("sample_data.csv","r").readlines():
	pointsX.append(int(i.split(",")[0]))
	pointsY.append(int(i.split(",")[1]))

hullX = [pointsX[0]] 
hullY = [pointsY[0]]

minX = pointsX[0]
maxX = pointsX[-1]

#Create subset of points above the line
S1X = []
S1Y = []
for i in range(1,len(pointsY)-2):
	if pointsY[i] > pointsY[-1] or pointsY[i] > pointsY[0]:
		S1X.append(pointsX[i])
		S1Y.append(pointsY[i])

maxS1Y = max(S1Y)
maxInd = [x for x in range(len(S1Y)) if S1Y[x] == maxS1Y]
print(maxInd) 

grad1 = grad(pointsX[0], S1X[maxInd], pointsY[0], S1Y[maxInd])
grad2 = grad(pointsX[-1], S1X[maxInd], pointsY[-1], S1Y[maxInd])

## Check gradient to see which points are included in the hull