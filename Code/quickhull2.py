import matplotlib.pyplot as plt
S = [[2,4],[3,6],[4,5],[5,7],[6,3],[7,1],[8,9],[9,2],[10,4]]
hull = [S[0],S[-1]] #Endpoints are always in the hull
def find_min(S):
	minInd = 0
	minVal = 1e4 
	for i in range(len(S)):
		if S[i][1] < minVal:
			minInd = i
			minVal = S[i][1]
	return minInd
def grad(x0,x1,y0,y1):
	return (y1-y0)/(x1-x0)
hull.insert(1, find_min(S))
m = S[find_min(S)]
testIndeces = [x for x in range(0,len(S)-1) if S[x][1]<min(S[0][1],S[-1][1])]
testSet = []
for i in testIndeces:
	testSet.append(S[i])
for i in testSet:
	if i == m:
		continue
	else:
		if grad(m[0],i[0],m[1],i[1]) > grad(m[0],S[0][0], m[1], S[0][1]):
			continue
		else:
			hull.append(i)

print(hull)

'''
sX = []
sY = []
hX = []
hY = []
for i in range(0,len(S)-1):
	sX.append(S[i][0])
	sY.append(S[i][1])
for i in range(0,len(hull)-1):
	hX.append(hull[i][0])
	hY.append(hull[i][1])
plt.plot(sX,sY, color = 'blue')
plt.plot(hX,hY, '--r')
plt.show()
'''