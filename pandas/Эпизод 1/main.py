import pandas as pd
from heapq import nlargest

df = pd.read_csv("transactions.csv")
print(df)

print(nlargest(3, list(df.loc[df['STATUS'] == 'OK', 'SUM']))) #выводит 3 максимальных значения в МАССИВЕ,
# но думаю это приемлимо

print(df.loc[df['STATUS'] == 'OK', ['CONTRACTOR', 'SUM']].groupby('CONTRACTOR').sum().loc['Umbrella, Inc', 'SUM'])
# а это полная сумма реально проведённых платежей в адрес Umbrella, Inc
