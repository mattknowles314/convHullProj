import math
import matplotlib.pyplot as plt

S = [[2,4],[3,6],[4,5],[5,7],[6,3],[7,1],[8,9],[9,2],[10,4]]

hull = [S[0],S[-1]] #Endpoints are always in the hull

def midpt(P,Q):
	return [0.5*(P[0]+Q[0]),0.5*(P[1]+Q[1])]

#Checks if a point is under or above a line
def furthestfromSeg(Sk, P, Q):
	midpnt = midpt(P,Q)
	distList = []
	for i in range(0,len(Sk)-1):
		distList.append(math.hypot(midpnt[1]-Sk[i][1],midpnt[0]-Sk[i][0]))
	m = distList.index(max(distList))
	hull.append(S[m+1])

#First we want to find the minimum point, as this will definately be in the convex hull

def find_min(S):
	minInd = 0
	minVal = 1e4 
	for i in range(len(S)):
		if S[i][1] < minVal:
			minInd = i
			minVal = S[i][1]
	return minInd

hull.insert(1, find_min(S)) #Insert this as the middle point in the hull

#Split into points on the left side of the min and rightside of the min

S1 = S[1:find_min(S)]
S2 = S[find_min(S)+1:len(S)-1]

#Check which ones are below the segment between start-min, min-end

furthestfromSeg(S1, S[0], S[find_min(S)])
furthestfromSeg(S2, S[find_min(S)], S[-1])

sX = []
sY = []
hX = []
hY = []
hull.remove(5)
S = sorted(S)
for i in range(0,len(S)):
	sX.append(S[i][0])
	sY.append(S[i][1])
for i in range(0,len(hull)):
	hX.append(hull[i][0])
	hY.append(hull[i][1])

plt.plot(sX,sY, color="blue")
plt.plot(hX,hY, '--r')
plt.show()