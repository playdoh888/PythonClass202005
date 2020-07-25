import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Employee": ["Susan", "Bart", "Emily", "Charles", "David", "Charles", "Julia", "Bart"],
    "City": ["London", "London", "Philadelphia", "London", "London", "Philadelphia", "London", "Philadelphia"],
    "Age": [20, 40, 18, 24, 37, 40, 44, 20],
    "Hours": [24, 40, 50, 36, 54, 44, 41, 35]})

print(df)

print(df.groupby(['Employee']).sum())
print(df.groupby('City').count())
print(df.groupby('Employee')['Hours'].sum().to_frame().reset_index().sort_values(by='Hours'))

plt.clf()
df.groupby('Employee').sum().plot(kind='bar')
plt.show()

print(df.groupby('Employee')['Age'].apply(lambda group_series: group_series.tolist()).reset_index())

print(df.groupby(['Employee']).mean())


def count_even_numbers(series):
    return len([elem for elem in series if elem % 2 == 0])


print(df.groupby('Employee')['Age'].apply(count_even_numbers).reset_index(name='num_even_numbers'))


df_filtered = df.query('Age < 30')
print(df_filtered)

