# Creating different Shapes
'''
So, we have created a program that draws a line 100 pixels long.
We can draw various shapes and fill different colors using turtle
methods. There’s plethora of functions and programs to be coded
using the turtle library in python. Let’s learn to draw some of the
basic shapes.

'''
import turtle
skk=turtle.Turtle()
#(1). Square:-
for i in range(4):
    skk.forward(50)#here 50 is the number of pixels by which turtle object moves forward.
    skk.right(90)#here 90 is the angle by which turtle object turns right
#turtle.done()
'''
#(2). star:-
angle=-50
for i in range(6):
    skk.right(angle)
    angle=50
    skk.forward(100)
turtle.done()
'''
skk.forward(100)
#(2). rectangle:-
size=150
changes=50
for i in range(4):
    skk.forward(size)
    size=size+(-changes)
    changes=-changes
    skk.right(90)
#turtle.done()

#(3). star:-
    
