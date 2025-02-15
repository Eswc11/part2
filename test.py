import pandas as pd
import numpy as np
# 1 exercises

# Scalar numbers
scalar_series = pd.Series(42)
print(scalar_series)

# List
list_series = pd.Series([1, 2, 3, 4, 5])
print(list_series)

# Tuple
tuple_series = pd.Series((10, 20, 30, 40))
print(tuple_series)

# Dictionary
dict_series = pd.Series({'a': 100, 'b': 200, 'c': 300})
print(dict_series)

# 2 exercises

months = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                   index=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
print("\nSeries with numbers month:")
print(months)

# 3 exercises

students = pd.Series({'MATDAIS': 36,'MATMIE': 32 , 'COMIE' : 35 , 'COMEC' : 31})
print('\nSeries with numbers students:')
print(students)

# 4 exercises

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df_data = pd.DataFrame(exam_data,index=labels)
print(df_data)

# 5 exercises

greater_df = df_data[df_data['attempts'] > 2]
print(greater_df)