import matplotlib.pyplot as plt
import os

f = open(os.path.join("dead_moroz", "005.dat"))
a = []
N = -1
i = 0
x = []
y = []
for line in f:
    if N == -1:
        N = int(line)
    else:
        a.append([float(j) for j in line.split()])

for i in range(N):
    x.append(a[i][0])
    y.append(a[i][1])

plt.figure(figsize=((max(x) - min(x))/100, (max(y) - min(y))/100))
plt.locator_params(axis='x', nbins=(max(x) - min(x))/50)
plt.locator_params(axis='y', nbins=(max(y) - min(y))/50)

plt.scatter(x, y, s=3)
plt.title('Number of points: ' + str(N))
plt.savefig("5.png")


plt.show()
