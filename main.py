import pandas as pd

print(f'\n1 TASK. Python library pandas base functions')
df1 = pd.read_csv("data/Weather_Radar_Stations.csv")

print(f'\nfirst five rows: \n{df1.head(5)}')
print(f'\ndata structure:')
df1.info()
print(f'\nstatistical description: \n{df1.describe()}')

print(f'\n2 TASK. Determination of average salary')
df2 = pd.read_csv("data/dz.csv")

group = df2.groupby('City')['Salary'].mean()
print(f'\nAverage salary:\n {group}')
