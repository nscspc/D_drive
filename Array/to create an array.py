'''
An array is a collection of items stored at contiguous memory locations.
The idea is to store multiple items of the same type together. This makes
it easier to calculate the position of each element by simply adding an offset to a base value, i.e.,
the memory location of the first element of the array (generally denoted by the name of the array).

'''

# 1st way to create an array using array function from array library .
import array as arr
a=arr.array('d',[1.2,10.2])
print(a)
print(type(a))
print()

'''
Here, we created an array of float type. The letter d is a type
code. This determines the type of the array during creation.

Commonly used type codes are listed as follows:

Code	C Type	Python Type	Min bytes
b	signed char	int	1
B	unsigned char	int	1
u	Py_UNICODE	Unicode	2
h	signed short	int	2
H	unsigned short	int	2
i	signed int	int	2
I	unsigned int	int	2
l	signed long	int	4
L	unsigned long	int	4
f	float	float	4
d	double	float	8

We will use two type codes in this entire article: i for integers
and d for floats.

'''
# 2nd way to create an array using array function from numpy library
import numpy as np
b=np.array([1,2,3,4,5])
print(b)
print(type(b))

'''
When to use arrays?

Lists are much more flexible than arrays.
They can store elements of different data types
including strings. And, if you need to do mathematical
computation on arrays and matrices, you are much
better off using something like NumPy.

So, what are the uses of arrays created from the
Python array module?

The array.array type is just a thin wrapper on C arrays
which provides space-efficient storage of basic C-style
data types. If you need to allocate an array that you
know will not change, then arrays can be faster and
use less memory than lists.

Unless you don't really need arrays (array module may be
needed to interface with C code), the use of the array module
is not recommended.

'''
