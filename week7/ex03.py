import pandas as pd

df = pd.read_csv('WPP2019_TotalPopulationBySex.csv')

print(df.axes)

print(df["PopMale"].mean())

print(df.groupby(['Location']).mean())





