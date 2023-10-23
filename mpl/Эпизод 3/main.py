import matplotlib.pyplot as plt
import statistics

f = open('students.csv')
a = []
preps = []
groups = []
mark = 3
for line in f:
    a.append([i for i in line.split(';')])

for i in range(len(a)):
    if preps.count(a[i][0]) == 0:
        preps.append(a[i][0])
    if groups.count(a[i][1]) == 0:
        groups.append(a[i][1])

values = []
for i in range(len(preps)):
    values.append([])
means = []
for i in range(8):
    means.append([])

valuesg = []
for i in range(len(groups)):
    valuesg.append([])
meansg = []
for i in range(8):
    meansg.append([])

for j in range(len(preps)):
    for i in range(len(a)):
        if a[i][0] == preps[j]:
            values[j].append(int(a[i][2]))

for j in range(len(groups)):
    for i in range(len(a)):
        if a[i][1] == groups[j]:
            valuesg[j].append(int(a[i][2]))

fig, ax = plt.subplots(nrows=2, ncols=2)

fig.set_figwidth(10)
fig.set_figheight(8)

plt.subplots_adjust(hspace=0.5)

while mark < 11:
    for i in range(len(preps)):
        means[mark-3].append(values[i].count(mark))
    for i in range(len(groups)):
        meansg[mark-3].append(valuesg[i].count(mark))
    mark += 1

mark = 3

while mark < 11:
    if mark == 3:
        ax[0][0].bar(preps, means[mark - 3], label=str(mark))
        ax[0][0].legend(loc=2, prop={'size': 6})
        mark += 1
    else:
        ax[0][0].bar(preps, means[mark - 3], bottom=means[mark - 4], label=str(mark))
        ax[0][0].legend(loc=2, prop={'size': 6})
        for i in range(len(means[0])):
            means[mark - 3][i] = means[mark - 3][i] + means[mark - 4][i]
        mark += 1

mark = 3

while mark < 11:
    if mark == 3:
        ax[1][0].bar(groups, meansg[mark - 3], label=str(mark))
        ax[1][0].legend(loc=2, prop={'size': 6})
        mark += 1
    else:
        ax[1][0].bar(groups, meansg[mark - 3], bottom=meansg[mark - 4], label=str(mark))
        ax[1][0].legend(loc=2, prop={'size': 6})
        for i in range(len(meansg[0])):
            meansg[mark - 3][i] = meansg[mark - 3][i] + meansg[mark - 4][i]
        mark += 1

averagepreps = [statistics.mean(i) for i in values]
averagegroups = [statistics.mean(i) for i in valuesg]
colorpreps = []
for i in averagepreps:
    if i == max(averagepreps):
        colorpreps.append('limegreen')
    elif i == min(averagepreps):
        colorpreps.append('r')
    else:
        colorpreps.append('gold')

colorgroups = []
for i in averagegroups:
    if i == max(averagegroups):
        colorgroups.append('limegreen')
    elif i == min(averagegroups):
        colorgroups.append('r')
    else:
        colorgroups.append('gold')

ax[0][1].bar(preps, averagepreps, color=colorpreps)
ax[1][1].bar(groups, averagegroups, color=colorgroups)

ax[0][0].set_title('Marks per prep')
ax[1][0].set_title('Marks per group')
ax[0][1].set_title('Average mark per prep')
ax[1][1].set_title('Average mark per group')

plt.savefig("statistics.png")

plt.show()



