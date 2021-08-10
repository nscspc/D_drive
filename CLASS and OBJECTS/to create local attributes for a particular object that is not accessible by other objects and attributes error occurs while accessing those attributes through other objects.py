class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')


# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method
# Output: 2+3j
num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10

# Output: (5, 0, 10)
print((num2.real, num2.imag, num2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
print(num1.attr)
Output

2+3j
(5, 0, 10)
'''Traceback (most recent call last):
  File "<string>", line 27, in <module>
    print(num1.attr)
AttributeError: 'ComplexNumber' object has no attribute 'attr'
In the above example, we defined a new class to
represent complex numbers. It has two functions
, __init__() to initialize the variables (defaults to zero)
and get_data() to display the number properly.

An interesting thing to note in the above step is that
attributes of an object can be created on the fly.
We created a new attribute attr for object num2
and read it as well. But this does not create that
attribute for object num1.
'''
