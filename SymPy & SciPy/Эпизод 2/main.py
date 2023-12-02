import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

f = open("large.txt")
N = int(f.readline())
a = np.loadtxt(f, dtype=np.float64)
b = np.array(a[-1], dtype=np.float64)
a = np.delete(a, [-1], 0)

x = linalg.solve(a, b)

plt.bar(np.arange(len(x)), x)
plt.grid()

plt.savefig("solved_SLAY.png")
plt.show()
