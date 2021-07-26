#Andrew's Monotone Chain Convex Hull
import sorting
import matplotlib.pyplot as plt

S = [[2,1],
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
L = []
U = []

def cross_product(o,a,b):
	return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

if len(S) <= 3:
	print("Error - Need more than 3 points")
else:
	for i in S:
		while len(L) >= 2 and cross_product(L[-2], L[-1], i) <= 0:
			L.pop()
		L.append(i)
'''
sX = []
sY = []
lX = []
lY = []

for i in S:
	sX.append(i[0])
	sY.append(i[1])
for i in L:
	lX.append(i[0])
	lY.append(i[1])

plt.plot(sX,sY, color="blue", label="f(x)")
plt.plot(lX,lY, '--r', label="CHull(f(x))")
plt.legend(loc="upper left")
plt.show()
'''