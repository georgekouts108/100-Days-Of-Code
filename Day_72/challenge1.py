import pandas as pd

salaries = pd.read_csv('salaries_by_college_major.csv')

rows, columns = salaries.shape
# print(f"{rows} rows, {columns} columns")
col_labels = salaries.columns
print(list(col_labels))

max_start_salary = salaries['Starting Median Salary'].max()
x = salaries[(salaries['Starting Median Salary'] == max_start_salary)]
print(f"{x['Undergraduate Major'].item()} has the higest starting salary (${x['Starting Median Salary'].item()})")

# q1
max_midcareer_salary = salaries['Mid-Career Median Salary'].max()
a = salaries[(salaries['Mid-Career Median Salary'] == max_midcareer_salary)]
print(f"{a['Undergraduate Major'].item()} has the higest mid-career salary (${a['Mid-Career Median Salary'].item()})")

# q2
min_start_salary = salaries['Starting Median Salary'].min()
b = salaries[(salaries['Starting Median Salary'] == min_start_salary)]
print(f"{b['Undergraduate Major'].item()} has the lowest starting salary (${b['Starting Median Salary'].item()})")

# q3
min_midcareer_salary = salaries['Mid-Career Median Salary'].min()
c = salaries[(salaries['Mid-Career Median Salary'] == min_midcareer_salary)]

for i in range(len(c)):
    print(f"{c.iloc[i]['Undergraduate Major']} has the lowest mid-career salary (${c.iloc[i]['Mid-Career Median Salary']})")



