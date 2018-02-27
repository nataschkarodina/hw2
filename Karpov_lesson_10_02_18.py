#Machine learning
#lesson 1 10.02.2018

import numpy as np
import pandas as pd

my_array = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])

#my_array

#pd.read_csv()

my_data = pd.DataFrame({'x': [1,2,3,4], 'y': [1,2,3,4], 'z':[1,2,3,4]})

my_data.describe()

print(my_data)

my_data.iloc[0:2, :]

my_data['x']
my_data.x

my_data[['x', 'y']]

my_data[my_data.y ==4]

my_data.query('y > 4')

my_data['new_var'] = np.array([1,2,3,4])

my_data = my_data.assign(new_var_2 = np.array([1,2,3,4]))

my_data.groupby('z', as_index=False).sum()
my_data.groupby('z', as_index=False).median()
my_data = my_data.groupby(['z', 'x'], as_index=False).median()
my_data.groupby('z', as_index=False).count()
my_data[['x', 'y']].groupby('z', as_index=False).count()\
    .sort_values('y')\
    .query('y' > 4)

my_data.sort_values('y')

my_data.drop(['new_var'], axis = 1)

print(my_data)
print ('smth')




