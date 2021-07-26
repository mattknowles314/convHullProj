import matplotlib.pyplot as plt

S=[[2,50],
[4,61],
[6,44],
[8,25],
[10,89],
[12,26],
[14,12],
[16,87],
[18,79],
[20,74],
[22,22],
[23,1],
[24,87],
[26,49],
[28,8],
[30,9],
[32,58],
[34,6],
[36,82],
[38,4],
[40,358],
[42,198],
[44,84],
[46,53],
[48,51],
[50,87],
[52,86],
[54,20],
[56,49]]
hull = [S[0]]

def grad(x0,x1,y0,y1):
	return (y1-y0)/(x1-x0)

def get_min(S):
	min_index = 0
	min_val = 100
	for i in range(0, len(S)-1):
		if S[i][1] <= min_val:
			min_val = S[i][1]
			min_index = i
	return min_index

def conv_hull(S):
	curr_point = 0
	while S[-1] not in hull:
		grads = []
		for i in range(curr_point, len(S)-1):
			grads.append(grad(S[curr_point][0],S[i+1][0],S[curr_point][1],S[i+1][1]))
		

		m = grads.index(min(grads))
		hull.append(S[curr_point+1+m])
		curr_point = curr_point+1+m



conv_hull(S)

sX = []
sY = []
lX = []
lY = []

for i in S:
	sX.append(i[0])
	sY.append(i[1])
for i in hull:
	lX.append(i[0])
	lY.append(i[1])

plt.plot(sX,sY, color="blue", label="f(x)")
plt.plot(lX,lY, '--r', label="CHull(f(x))")
plt.legend(loc="upper left")
plt.show()