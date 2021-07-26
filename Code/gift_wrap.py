import matplotlib.pyplot as plt
pointsX = []
pointsY = []

points = [[3,2],[4,5]]

for i in open("sample_data.csv","r").readlines():
	pointsX.append(int(i.split(",")[0]))
	pointsY.append(int(i.split(",")[1]))

def plot_hull(pointsX, pointsY, hullX, hullY):
	plt.plot(pointsX,pointsY, 'b', label="f(x)")
	plt.plot(hullX, hullY, '--r', label="CHull(f(x))")
	plt.legend(loc="upper left")
	plt.show()

hullX = []
hullY = []

t = len(pointsX)
l = 0
hullX.append(pointsX[l])
hullY.append(pointsY[l])
while(True):
	q = (l+1) % t
	for i in range(t):
		if i == l:
			continue
		d = direction(points)