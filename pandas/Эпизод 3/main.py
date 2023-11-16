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

data1 = data.groupby(['group_faculty']).sum().loc[:, 'Solved']
data2 = data.groupby('group_out').sum().loc[:, 'Solved']

fig, axes = plt.subplots(2)
fig.set_figwidth(9)
fig.set_figheight(12)
plt.subplots_adjust(hspace=0.5)

data1.plot(kind='bar', ax=axes[0], title='Average solved tasks per fuculty group')
data2.plot(kind='bar', ax=axes[1], title='Average solved tasks per inf group')
plt.savefig("statistics.png")

plt.show()

print("======================================")
best = data[(data['H'] > 9) | (data['G'] > 9)].loc[:, ['group_faculty', 'group_out']]
print("The best students in this groups:")
print(best.group_faculty.unique())
print(best.group_out.unique())
