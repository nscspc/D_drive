# to print data in tabular form ( or in a dataframe )
import numpy as np
from sklearn.datasets import load_boston
import pandas

df=load_boston()

boston=pandas.DataFrame(df.data,columns=df.feature_names)#boston is the variable in which whole data is made to store in tabular form.

boston.head()#head() function return the dataframe of top 5 rows. #we can write boston.head(100) to print 100 lines of data.

'''
output : in jupyter notebook

            CRIM	ZN	INDUS	CHAS	NOX	RM	AGE	DIS	RAD	TAX	PTRATIO	   B	LSTAT
0	0.00632	18.0	2.31	0.0	0.538	6.575	65.2	4.0900	1.0	296.0	15.3	396.90	4.98
1	0.02731	0.0	7.07	0.0	0.469	6.421	78.9	4.9671	2.0	242.0	17.8	396.90	9.14
2	0.02729	0.0	7.07	0.0	0.469	7.185	61.1	4.9671	2.0	242.0	17.8	392.83	4.03
3	0.03237	0.0	2.18	0.0	0.458	6.998	45.8	6.0622	3.0	222.0	18.7	394.63	2.94
4	0.06905	0.0	2.18	0.0	0.458	7.147	54.2	6.0622	3.0	222.0	18.7	396.90	5.33

'''
# to add a new column to the dataframe variable 'boston' :-
boston['medv']=df.target # medv is the name of the column .
boston.head()
'''
output:

CRIM	ZN	INDUS	CHAS	NOX	RM	AGE	DIS	RAD	TAX	PTRATIO	B	LSTAT	medv
0	0.00632	18.0	2.31	0.0	0.538	6.575	65.2	4.0900	1.0	296.0	15.3	396.90	4.98	24.0
1	0.02731	0.0	7.07	0.0	0.469	6.421	78.9	4.9671	2.0	242.0	17.8	396.90	9.14	21.6
2	0.02729	0.0	7.07	0.0	0.469	7.185	61.1	4.9671	2.0	242.0	17.8	392.83	4.03	34.7
3	0.03237	0.0	2.18	0.0	0.458	6.998	45.8	6.0622	3.0	222.0	18.7	394.63	2.94	33.4
4	0.06905	0.0	2.18	0.0	0.458	7.147	54.2	6.0622	3.0	222.0	18.7	396.90	5.33	36.2

'''

# .isnull( ) :- it is used to find out the null values in the datasets :-
boston.isnull()

'''
      CRIM     ZN  INDUS   CHAS    NOX     RM    AGE    DIS    RAD    TAX  \
0    False  False  False  False  False  False  False  False  False  False   
1    False  False  False  False  False  False  False  False  False  False   
2    False  False  False  False  False  False  False  False  False  False   
3    False  False  False  False  False  False  False  False  False  False   
4    False  False  False  False  False  False  False  False  False  False   
..     ...    ...    ...    ...    ...    ...    ...    ...    ...    ...   
501  False  False  False  False  False  False  False  False  False  False   
502  False  False  False  False  False  False  False  False  False  False   
503  False  False  False  False  False  False  False  False  False  False   
504  False  False  False  False  False  False  False  False  False  False   
505  False  False  False  False  False  False  False  False  False  False   

     PTRATIO      B  LSTAT   medv  
0      False  False  False  False  
1      False  False  False  False  
2      False  False  False  False  
3      False  False  False  False  
4      False  False  False  False  
..       ...    ...    ...    ...  
501    False  False  False  False  
502    False  False  False  False  
503    False  False  False  False  
504    False  False  False  False  
505    False  False  False  False  

'''

# isnull( ).sum( ) :- it will print the total no. of null value with respect to columns (or grouped by columns)
print(boston.isnull( ).sum( ))

'''
[506 rows x 14 columns]
CRIM       0
ZN         0
INDUS      0
CHAS       0
NOX        0
RM         0
AGE        0
DIS        0
RAD        0
TAX        0
PTRATIO    0
B          0
LSTAT      0
medv       0
dtype: int64

'''
from sklearn.model_selection import train_test_split # train_test_split funtion will help us to divide the entire data into training data and testing data.

#now dividing data into 2 parts:-

# (1). x represents whole dataframe except medv column .
'''
x is a dataframe which contains all the columns except 'medv' column
because x is going to be used to predict the medv column ,and medv column will be calling it as y.
x is also a dataframe

'''
x=boston.drop('medv',axis=1)# drop( ) function is used to delete a column , and axis=1 is used for a column and axis=0 is used for a row.
'''
from a copy of boston dataframe medv column is dropped (not from actual boston )
and then that resultant copy is assigned to variable(dataframe) x .
'''

# (2). y represents the target values .
y=boston['medv']

'''
x is used to predict y

'''
#now we are creating training and testing part :-
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.15,random_state=5)
'''
x_train,x_test,y_train,y_test => this combination of variable separated by ','
behaves like a tuple.

in function x,y is put in as input to the train_test_split function
to split data into train and test.

test_size specifies the no. of test questions , here 15 questions are taken as test out of 100 questions(data points)
and rest of the questions(data) is left for training.

random_state provides a random datapoints for training purpose and testing purpose.

'''
#.shape will provide the no. of rows and columns in the training and testing sets
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression
'''
Linear regression attempts to model the relationship between 2 variables
by fitting a linear equation to observed data .
A linear regression has an equation of the form y=a+bx , where x is the
explanatory variable and y is the dependent variable.
'''
from sklearn.metrics import mean_squared_error
'''
mean_squared_error is to find out the error between
the predicted value and what we expect from it
'''
# to create linear regression model
lin_model=LinearRegression()#now machine learning algorithm has been made by writing this line.

#now we have to feed the training dataset(guide) to model(students)
lin_model.fit(x_train,y_train)

# now we have trained the entire model and now we have to predict it :-
y_train_predict=lin_model.predict(x_train)
'''
predict function is used to predict by using x_train dataset
it will provide the predict value which is equivalent to y_train dataset.
'''
#now finding out error between predicted and expected :-
rmse=(np.sqrt(mean_squared_error(y_train,y_train_predict)))# rmse=root mean square error.

print("\nthe model performance for training set")
print('RMSE is {}'.format(rmse))

#now on testing data previously we have done it on training data itself :-
y_test_predict=lin_model.predict(x_test)
'''
here we are going to  use x_test to predict the y_test.
here x_test is the unseend data as we have not provided it
to the machine learning model.
'''
rmse=(np.sqrt(mean_squared_error(y_test,y_test_predict)))

print("\nthe model performance for testing set")
print('RMSE is {}'.format(rmse))

'''
output :-

the model performance for training set
RMSE is 4.710901797319796

the model performance for testing set
RMSE is 4.687543527902947

'''
# as we can see that there is not big error
# it is a very small error.
# the model performed very well and beautifully .

#now visualizing the error using graph :-

import matplotlib.pyplot as plt

plt.figure(figsize=(100,5))#this figure function is used to specify the size of the figure window while executing .
plt.scatter(y_test,y_test_predict)#scatter function is used to plot the intersection of y_test & y_test_predict .
plt.plot([min(y_test_predict),max(y_test_predict)],[min(y_test_predict),max(y_test_predict)],"r")# plot function is used to plot line graph .
plt.xlabel("actual")
plt.ylabel("predicted")
plt.show( )
