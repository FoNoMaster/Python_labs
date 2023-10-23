import matplotlib.pyplot as plt

f = open('dead_moroz\\004.dat')
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

plt.scatter(x, y, s=5)
plt.title('Number of points: ' + str(N))
plt.savefig("4.png")
plt.show()
