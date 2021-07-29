import matplotlib.pyplot as plt
S = [[2,4],[3,6],[4,2],[5,7],[6,3],[7,3],[8,9],[9,2],[10,4],[11,6],[12,8]]
hull = [S[0]] #Endpoints are always in the hull
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

def quickHull(S):
	m = S[find_min(S)]
	hull.append(m)
	k = min(S[0][1], S[-1][1])

	S1 = []
	S2 = []
	for i in range(1,find_min(S)-1):
		if S[i][1] <= k:
			S1.append(S[i]) 
	for i in range(find_min(S)+1, len(S)-1):
		if S[i][1] <= k:
			S2.append(S[i])

	while len(S1)!=0:
		for i in S1:
			if grad(m[0],i[0],m[1],i[1]) > grad(m[0],S[0][0], m[1], S[0][1]):
				hull.append(i)
				S1.remove(i)
			else:
				S1.remove(i)

	while len(S2)!=0:
		for i in S2:
			if grad(i[0],S[-1][0],i[1],S[-1][1]) > grad(m[0],S[-1][0], m[1], S[-1][1]):
				hull.append(i)
				S2.remove(i)
			else:
				S2.remove(i)
	hull.append(S[-1])
'''
S = sorted(S)
hull = sorted(hull)
sX = []
sY = []
hX = []
hY = []
for i in range(0,len(S)):
	sX.append(S[i][0])
	sY.append(S[i][1])
for i in range(0,len(hull)):
	hX.append(hull[i][0])
	hY.append(hull[i][1])
plt.plot(sX,sY, color = 'blue')
plt.plot(hX,hY, '--r')
plt.show()
'''