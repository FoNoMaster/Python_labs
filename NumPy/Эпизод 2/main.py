import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("signal03.dat", dtype=np.float64)
data1 = np.convolve(data, np.ones(10))
data1 = np.delete(data1, np.arange(len(data), len(data1)))

data1[:10] = data1[:10] / np.arange(1, 11)
data1[10:] = data1[10:] / 10

fig, ax = plt.subplots(nrows=1, ncols=2)
fig.set_figwidth(10)
fig.set_figheight(6)
ax[0].plot(data)
ax[1].plot(data1)
ax[0].grid()
ax[1].grid()
ax[0].set_title('Сырой сигнал')
ax[1].set_title('После фильтра')
plt.savefig("signal_3")
plt.show()

