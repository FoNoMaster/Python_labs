import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("flights.csv")
print(df)
cargos = []
for i in range(len(df)):
    if cargos.count(df.iloc[i, 1]) == 0:
        cargos.append(df.iloc[i, 1])
print(cargos)

flytimes = [0 for i in range(len(cargos))]

for i in range(len(df)):
    for j in range(len(cargos)):
        if df.iloc[i, 1] == cargos[j]:
            flytimes[j] = flytimes[j] + 1
print(flytimes)

data1 = df.loc[:, ['CARGO', 'WEIGHT']].groupby('CARGO').sum()
print(data1)

data2 = df.loc[:, ['CARGO', 'PRICE']].groupby('CARGO').sum()
print(data2)

data3 = pd.DataFrame(flytimes, index=cargos)

ax = data1.plot(kind='bar')
ax.set_xlabel('COMPANY')
ax.set_ylabel('WEIGHT')

# bx = data2.plot(kind='bar')
# bx.set_xlabel('COMPANY')
# bx.set_ylabel('PRICE')

# cx = data3.plot(kind='bar')
# cx.set_xlabel('COMPANY')
# cx.set_ylabel('NUMBER OF FLIGHTS')

plt.savefig("WEIGHT.png")
plt.show()
