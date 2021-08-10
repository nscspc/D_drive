# pandas library :-
'''
=> to create a series using a list or array or dictionary or tuple with user defined index in the form of 1d array .
=> to create a data structure in the form of 2d array .

'''

import pandas as pd
x=[1,2,3,4,5]
s=pd.Series(x)
print("pandas series : \n",s)

'''
output :-

pandas series : 
 0    1
1    2
2    3
3    4
4    5
dtype: int64

'''
