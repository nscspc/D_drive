# hexagon :-
import turtle
window=turtle.Screen()
window.title("hexagon")

cursor=turtle.Turtle()
cursor.speed(0)
for i in range(6):
    cursor.right(60)
    cursor.forward(100)
    cursor.fillcolor("yellow")
cursor.penup()
for i in range(6):
    cursor.right(60)
    cursor.forward(100)
cursor.pendown()
cursor.ht()
'''
num_sides = 6
side_length = 70
angle = 360.0 / num_sides # to find out the angle according to the no. of the sides.
'''
