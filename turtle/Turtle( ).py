# Turtle( ):-
'''
Turtle( ) function is used to create and returning a new
turtle object.

'''
import turtle
window=turtle.Screen()#for making a screen
window.bgcolor("light green")#for background
window.title("turtle window")#for the title of the window
skk=turtle.Turtle()

#forward(amount):-
'''
moves the turtle forward by the specified amount
=> now that we have created the window and the turtle, we
    need to move the turtle.
    ->to move forward 100 pixels in the direction skk is facing.
'''
skk.forward(100)
#backward(amount):-
'''
moves the turtle backward by the specified amount.
=> now that we have created the window and the turtle, we
    need to move the turtle.
    ->to move backward 100 pixels in the direction skk is facing.
'''
skk.backward(100)

#done( ):-
'''
we have moved skk , now we have to complete the program with
the done( ) function.
'''
turtle.done()

#right(angle):-
'''
turns the turtle clockwise.
'''
#left(angle):-
'''
turns the turtle counter clockwise.
'''
#penup():-
'''
picks up the turtle's pen
'''
