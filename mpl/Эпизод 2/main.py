import matplotlib.pyplot as plt

f = open('lms.mipt.ru_pluginfile.php_168477_mod_assign_intro_frames.dat.txt')
x = []
y = []
i = 0
minx = 0
miny = 0
maxx = 0
maxy = 0

for line in f:
    if i == 0:
        x.append([float(j) for j in line.split()])
        i = 1
    else:
        y.append([float(j) for j in line.split()])
        i = 0

for j in range(len(x)):
    for k in range(len(x[j])):
        if x[j][k] < minx:
            minx = x[j][k]
        if x[j][k] > maxx:
            maxx = x[j][k]
        if y[j][k] < miny:
            miny = y[j][k]
        if y[j][k] > maxy:
            maxy = y[j][k]


fig, ax = plt.subplots(nrows=3, ncols=2)

fig.set_figwidth(10)
fig.set_figheight(10)

plt.subplots_adjust(wspace=0.3, hspace=0.5)

for i in range(len(x)):
    ax[i//2, i % 2].plot(x[i], y[i])
    ax[i//2, i % 2].set_title('Frame ' + str(i))
    ax[i//2, i % 2].locator_params(axis='x', nbins=8)
    ax[i//2, i % 2].locator_params(axis='y', nbins=11)
    ax[i//2, i % 2].grid()
    ax[i//2, i % 2].set_xlim(minx, maxx)
    ax[i//2, i % 2].set_ylim(miny - 1, maxy + 1)

plt.savefig("frames.png")
plt.show()
