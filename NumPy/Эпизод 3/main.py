import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = np.loadtxt("mod_assign_intro_start.dat.txt", dtype=np.float64)

fig, ax = plt.subplots()
ax.set_xlim(0, 51)
ax.set_ylim(0, 10)
ax.grid()

E = np.diag(np.ones(data.size))
A = E + np.roll(-E, 1, 0)
line, = ax.plot(data)


def animate(i):
    global data
    if i > 0:
        line.set_ydata(data)
        data = np.matmul(E - A / 2, data)
    return line,


anim = animation.FuncAnimation(fig, animate, frames=255, interval=20)
Writer = animation.PillowWriter(fps=30)
anim.save('process.gif', writer=Writer)
