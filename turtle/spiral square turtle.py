import turtle   #Outside_In
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()
skk.color("blue")

side=100
for i in range(30):
    skk.forward(side)
    side-=4
    skk.left(90)
turtle.done()
