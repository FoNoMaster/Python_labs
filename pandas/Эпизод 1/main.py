import pandas as pd

df = pd.read_csv("transactions.csv")
print(df)

print("\n3 самых крупных платежа из реально проведённых:", end=' ')
print(list(df.loc[df['STATUS'] == 'OK', ['CONTRACTOR', 'STATUS', 'SUM']].nlargest(3, ['SUM']).loc[:, 'SUM']))

print("Полная сумма реально проведённых платежей в адрес Umbrella, Inc:", end=' ')
print(df.loc[df['STATUS'] == 'OK', ['CONTRACTOR', 'SUM']].groupby('CONTRACTOR').sum().loc['Umbrella, Inc', 'SUM'])
