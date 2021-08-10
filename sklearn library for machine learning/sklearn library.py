from sklearn.datasets import load_boston
'''
scikit(sk) learn is a python library which is used in
prediction and all and ml  , it contains datasets which it uses
to complete the tasks .
load_boston is the function of module datasets which contains information
or data in it

'''
df=load_boston()
'''
load_boston function contains data in the form of dictionary
therefore df is equivalent to dictionary

'''

print(type(df),'\n\n')

print(df.keys(),'\n\n')

print(df.data,'\n\n')# it contains list of list of data of the particular column

print(df.target,'\n\n')# target contains the list of cost ( or data ) which is used to predict data.

print(df.feature_names,'\n\n')# to print all the names of the columns.

print(df.DESCR,'\n\n')# to print description of df .

print(df.filename,'\n\n')# it print the location of the file where it is stored.
