from sklearn.mode_selection import train_test_split # train_test_split funtion will help us to divide the entire data into training data and testing data.

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
lin_model.fit(x_train,Y_train)

# now we have trained the entire model and now we have to predict it :-
Y_train_predict=lin_model.predict(x_train)
'''
predict function is used to predict by using x_train dataset
it will provide the predict value which is equivalent to y_train dataset.
'''
#now finding out error between predicted and expected :-
rmse=(np.sqrt(mean_squared_error(y_train,Y_train_predict)))# rmse=root mean square error.

print("the model performance for training set")
print(RMSE is {}.format(rmse))

#now on testing data previously we have done it on training data itself :-
y_test_predict=lin_model.(x_test)
'''
here we are going to  use x_test to predict the y_test.
here x_test is the unseend data as we have not provided it
to the machine learning model.
'''
rmse=(np.sqrt(mean_squared_error(y_test,y_test_predict)))

print(RMSE is {}.format(rmse))
