import pandas as pd
import matplotlib.pyplot as plt

st_info = pd.read_excel("students_info.xlsx")
st_info.rename(columns={'login': 'User'}, inplace=True)
print(st_info)

print("=====================================")
kr = pd.read_html("results_ejudge.html")[0]
print(kr)

print("=====================================")
data = pd.merge(st_info, kr, on='User')
print(data)

fuculty_group = [i for i in data.groupby('group_faculty').sum().index]
out_group = [i for i in data.groupby('group_out').sum().index]

fuculty_average = []
for i in fuculty_group:
    fuculty_average.append(data.loc[data['group_faculty'] == i, 'Solved'].mean())

group_average = []
for i in out_group:
    group_average.append(data.loc[data['group_out'] == i, 'Solved'].mean())

fig, ax = plt.subplots(nrows=2)
plt.subplots_adjust(hspace=0.5)


ax[0].bar([str(i) for i in fuculty_group], fuculty_average)
ax[1].bar([str(i) for i in out_group], group_average)
ax[0].set_title('Solved tasks per fuculty group')
ax[1].set_title('Solved tasks per inf group')
plt.savefig("statistics.png")

plt.show()

print("======================================")
fuc = []
inf = []
best = data[(data['H'] > 9) | (data['G'] > 9)].loc[:, ['group_faculty', 'group_out']]
for i in range(len(best)):
    if fuc.count(best.iloc[i, 0]) == 0:
        fuc.append(best.iloc[i, 0])
    if inf.count(best.iloc[i, 1]) == 0:
        inf.append(best.iloc[i, 1])
print("The best students in this groups:")
print(fuc)
print(inf)

