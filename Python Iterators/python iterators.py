# iteration :-
'''
Iteration is the repetition of a process in order
to generate an outcome. The sequence will approach
some end point or end value. Each repetition of the
process is a single iteration, and the outcome of each
iteration is then the starting point of the next iteration.

What is an example of iteration?
Iteration is when the same procedure is repeated
multiple times. Some examples were long division,
the Fibonacci numbers, prime numbers, and the
calculator game. Some of these used recursion
as well, but not all of them. bunch of successive
integers, or repeat a procedure a given number of times.

'''

#Iterators in Python
'''
Iterator in python is an object that is used to
iterate over iterable objects like lists, tuples,
dicts, and sets. The iterator object is initialized
using the iter() method. It uses the next() method for iteration.
 
[1] => __iter(iterable)__ method that is called for the
        initialization of an iterator. This returns an iterator object
[2] => next ( __next__ in Python 3) The next method returns
        the next value for the iterable. When we use a for loop
        to traverse any iterable object, internally it uses the
        iter() method to get an iterator object which further
        uses next() method to iterate over. This method
        raises a StopIteration to signal the end of the iteration.
'''
#return an iterator from a tuple and print each value :-
mytuple=("apple","banana","cherry")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit),"\n")

# strings are also iterable objects , containing a sequence of characters :-
mystr="abcd"
myit=iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit),"\n")

#Loopinf through an iterator :-
'''
we can also use a for loop to iterate through an iterable object :-
'''
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)
print()

# Creating an Iterator :-
'''
to create an object/class as an iterator we have to implement the
methods __iter__( ) and __next__( ) to the object .

__iter__( ) method acts similar to __init__( ) method , we can do
operations (like initializing ,etc) , but must always return the
iterator object itself.

__next__( ) method also allwos us to do operations , and must return
the next item in the sequence.

'''

class mynumbers:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        x=self.a
        self.a+=1
        return x

myobject=mynumbers( )
myit=iter(myobject)
        #print(iter(myobject)) => output :- <__main__.mynumbers object at 0x03921930>
print(next(myit))#as we are using next function so the value returned by __next__( ) is printed.
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit),"\n")

# StopIteration :-
'''
the program above would continue forever if we had enough next( )
statements, or if it was used in a for loop.

to prevent the iteration to go on forever , we can use the
StopIteration statement.

in the __next__( ) method , we can add a terminating condition
to raise an error if the iteration is done a specified number
of times .

'''
'''
class numbers:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        if self.a<=20:
            x=self.a    
            self.a +=1
            print(x)
            return self.a
        else:
            raise StopIteration

myobject=numbers( )
# myit=iter(myobject) => output :- <__main__.numbers object at 0x0414EE70>
print(myit)
for x in myit:
    print(next(myit))
'''

#for output 1,2,3,4,5.....
class numbers:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        if self.a<=20:
            x=self.a    
            self.a +=1
            if(x%2!=0):
                print(x)
            return x
        else:
            raise StopIteration

myobject=numbers( )
myit=iter(myobject) #=> output :- <__main__.numbers object at 0x0414EE70>
print(myit)
for x in myit:
    print(next(myit))
print( )
#Iterating Through an Iterator
'''
We use the next() function to manually iterate through all
the items of an iterator. When we reach the end and
there is no more data to be returned, it will raise the
StopIteration Exception. Following is an example.

'''
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

# Output: 4
print(next(my_iter))

# Output: 7
print(next(my_iter))

# next(obj) is same as obj.__next__()

# Output: 0
print(my_iter.__next__())

# Output: 3
print(my_iter.__next__())

# This will raise error, no items left
next(my_iter)


#Working of for loop for Iterators:-
'''
As we see in the above example, the for loop was able to
iterate automatically through the list.

In fact the for loop can iterate over any iterable.
Let's take a closer look at how the for loop is actually
implemented in Python.

for element in iterable:
    # do something with element
Is actually implemented as.

'''
# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break

'''
So internally, the for loop creates an iterator object,
iter_obj by calling iter() on the iterable.

Ironically, this for loop is actually an infinite while loop.

Inside the loop, it calls next() to get the next element
and executes the body of the for loop with this value.
After all the items exhaust, StopIteration is raised
which is internally caught and the loop ends. Note
that any other kind of exception will pass through.

'''
#Python Infinite Iterators
'''
It is not necessary that the item in an iterator object
has to be exhausted. There can be infinite iterators
(which never ends). We must be careful when handling
such iterators.

Here is a simple example to demonstrate infinite iterators.

The built-in function iter() can be called with two
arguments where the first argument must be a callable
object (function) and second is the sentinel. The iterator
calls this function until the returned value is equal to the sentinel.

>>> int()
0

>>> inf = iter(int,1)
>>> next(inf)
0
>>> next(inf)
0

We can see that the int() function always returns 0.
So passing it as iter(int,1) will return an iterator that
calls int() until the returned value equals 1. This never
happens and we get an infinite iterator.

We can also build our own infinite iterators. The following
iterator will, theoretically, return all the odd numbers.

'''
class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

'''
A sample run would be as follows.

output:

>>> a = iter(InfIter())
>>> next(a)
1
>>> next(a)
3
>>> next(a)
5
>>> next(a)
7

'''
