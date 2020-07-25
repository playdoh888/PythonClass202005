# Import pandas
import pandas as pd

# reading csv file
df = pd.read_csv("WPP2019_TotalPopulationBySex.csv")


pd.set_option('display.max_rows', None)
print(df.groupby(['Location'])['PopMale'].mean())





# print("World Average Population Break Down:")
# print(df[['Location', 'PopMale', 'PopFemale']].mean())

