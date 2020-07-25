import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Employee": ["Susan", "Kevin", "Charles", "David", "Ben"],
    "Salary": [60000, 35000, 31000, 10000, 20000],
    "Year": [2019, 2019, 2019, 2019, 2019]})

print(df)

df_filtered = df.query('Salary > 30000')
print(df_filtered)


df = pd.DataFrame({
    "Employee": ["Susan", "Bart", "Emily", "Charles", "David", "Charles", "Julia", "Bart"],
    "City": ["London", "London", "Philadelphia", "London", "London", "Philadelphia", "London", "Philadelphia"],
    "Age": [20, 40, 18, 24, 37, 40, 44, 20],
    "Hours": [24, 40, 50, 36, 54, 44, 41, 35]})

df['sum']=df.groupby(['Employee'])['Age'].transform('sum')
print(df)
