import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

f = open("large.txt")
N = int(f.readline())
a = np.array([np.ones(N)], dtype=np.float64)
for line in f:
    a = np.append(a, [[float(j) for j in line.split()]], 0)
b = np.array(a[-1], dtype=np.float64)
a = np.delete(a, [0, -1], 0)

x = linalg.solve(a, b)

plt.bar(np.arange(len(x)), x)
plt.grid()

plt.savefig("solved_SLAY.png")
plt.show()
