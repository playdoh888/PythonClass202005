import pandas as pd
import matplotlib.pyplot as plt


plt.clf()
df = pd.read_csv('WPP2019_TotalPopulationBySex.csv')

print(df.axes)

print(df["PopMale"].mean())

print("Average Population: ")
# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.options.display.float_format = '{:,.2f}'.format
# print(df.groupby('Location')['PopMale'].mean())
df.groupby('Location')['PopMale'].mean().plot(kind='bar')
plt.show()





