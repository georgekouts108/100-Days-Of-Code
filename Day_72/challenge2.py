import pandas as pd

salaries = pd.read_csv('salaries_by_college_major.csv')
col_labels = salaries.columns

tenth = salaries['Mid-Career 10th Percentile Salary']
ninetieth = salaries['Mid-Career 90th Percentile Salary']

differences = abs(tenth.values - ninetieth.values)
salaries.insert(loc=5, column='Spread', value=differences)
low_risk_majors = salaries.sort_values(by='Spread')
print(low_risk_majors[['Undergraduate Major', 'Spread']])

# q1
x = low_risk_majors[['Undergraduate Major', 'Spread']]
highest_potentials = x[(x['Spread'] == x['Spread'].min())]
print(f"Degrees with highest potential = {highest_potentials['Undergraduate Major'].values}")

# q2
y = salaries.sort_values(by='Mid-Career 90th Percentile Salary')
y = y[(y['Mid-Career 90th Percentile Salary'].isna() == False)]
result = y.tail()
print(result)

# q3
z = salaries[(salaries['Spread'].isna() == False)]
greatest_spread = z[(salaries['Spread'] == salaries['Spread'].max())]
result2 = greatest_spread[['Undergraduate Major', 'Spread']]
print(result2)
