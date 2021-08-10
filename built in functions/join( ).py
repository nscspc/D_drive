print("bb".join('aaaa'))
'''
output:

abbabbabba

each element is of 'aaaa' is separated by 'bb'

'''
# .join( ) with list
x=[1,2,3,4]#only string is processed in join( ) otherwise error
x=['1','2','3','4']
separator=','
print(separator.join(x))

# .join( ) with tuple
x=('1','2','3','4')
separator=','
print(separator.join(x))

# .join( ) with sets
x={'1','2','3'}
s=','
print(s.join(x))

x={'python','java','ruby'}
s='->->'
print(s.join(x))

# .join( ) with dictionaries
test={'mat':1,'that':2}
s='->'
print(s.join(test))

test={1:'mat',2:'that'}
s=','
print(s.join(test))#error : as since keys are not string
