import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("flights.csv")
df.loc[:, 'NUMBER OF FLIGHTS'] = 1
print(df)

data = df.groupby('CARGO').sum()
print(data)

data[['PRICE', 'WEIGHT', 'NUMBER OF FLIGHTS']].plot(kind='bar', subplots=True, figsize=(10, 20))

plt.savefig("statistics.png")
plt.show()
