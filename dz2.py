import pandas as pd

data_classes = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph'],
    'Science': [5, 3, 5, 4, 3, 3, 5, 4, 4, 5],
    'Physical Education': [5, 4, 5, 4, 5, 4, 5, 4, 5, 5],
    'Math': [5, 3, 4, 3, 4, 3, 4, 4, 3, 5],
    'Arts': [5, 5, 4, 4, 5, 3, 4, 4, 5, 4],
    'History': [5, 3, 4, 4, 4, 5, 5, 3, 3, 3]
}

df = pd.DataFrame(data_classes)

print(f'\nTest dataset:\n{df.head(4)}')
print(f'\nTest dataset length: {len(df)}\n')

for i in ['Science', 'Physical Education', 'Math', 'Arts', 'History']:
    print(f'{i}: average mark = {df[i].mean()}, median mark = {df[i].median()}, standard deviation = {df[i].std():.2f}')

Q1_math = df['Math'].quantile(0.25)
Q3_math = df['Math'].quantile(0.75)
IQR = Q3_math - Q1_math
downside = Q1_math - 1.5 * IQR
upside = Q3_math + 1.5 * IQR

print(f'\nQ1_math: {Q1_math}, Q3_math: {Q3_math}, downside: {downside}, upside: {upside}')

df_new = df[(df['Math'] >= downside) & (df['Math'] <= upside)]
print(f'\nTest data set after removing math outliers:\n{df_new.head(4)}')
print(f'\nTest dataset length: {len(df_new)}')

