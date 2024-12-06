import pandas as pd

salaries = pd.read_csv('salaries_by_college_major.csv')
col_labels = salaries.columns
print(list(col_labels))

s = salaries.groupby('Group')
print(s.mean('Spread'))