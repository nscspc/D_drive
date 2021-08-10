import turtle
import random
import time

delay=0.1
score=0
highestscore=0

#snakebody
bodies=[]

#getting a screen : canvas
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("black")
s.setup(width=500,height=500)

#create snake head
head=turtle.Turtle()
head.speed(1000000**1000000)
head.shape("square")
head.color("yellow")
head.fillcolor("yellow")
head.penup()
head.goto(0,0)
head.direction="stop"#here we have taken a variable direction whose value we have given is 'stop' .

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.fillcolor("yellow")
food.penup()# penup( ){picks up turtle's pen} :- basically makes sure that the moving object that we have created does not draw anything on the window.
#food.ht()#ht function is used to hide the turtle(which draws the figures)
food.goto(0,200)
#food.st()#st is show turtle which is used to show the turtle object.

#score board
sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-200,-200)#here we have set the position of the turtle in extreme left and bottom
sb.write("score:0 highest score:0")# here we have used write function to write something on the screen.

#now we are making the function for the movement of the body according to the condition that the snake cannot cross itself.
def moveup():#if the direction of the snake in not down then only it can move up
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def movestop():
    head.direction="stop"

def move():#to move the body according to the key pressed.
    if head.direction=="up":
        y=head.ycor()#here using the ycor( ) , we are obtaining the current position(y-coordinate) of the snake head. 
        head.sety(y+20)#and the adding 20 in the current position.
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)        
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#Event Handling - key mappings
s.listen()
s.onkey(moveright,"Right")#onkey( ) function is used to map  the keys according to the keys pressed => syntax-> s.onkey( function_name , signature_of_the_key ) .
s.onkey(moveleft,"Left")
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(movestop,"space")

#main loop
while True:
    s.update()# here we have used the update function so that the screen gets updated again and again.
    # checking collision with border so that it can come from the opposite side.
    if head.xcor()>240:
        head.setx(-240)
    if head.xcor()<-240:
        head.setx(240)
    if head.ycor()>240:
        head.sety(-240)
    if head.ycor()<-240:
        head.sety(240)

    #checking collision with food
    if head.distance(food)<20:
        # to move the food to new random coordinate.
        x=random.randint(-240,240)
        y=random.randint(-240,240)
        food.goto(x,y)
        # to increase the length of the snake.
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("triangle")
        body.color("yellow")
        body.fillcolor("yellow")
        bodies.append(body)#we are adding the body to the bodies(list) .
        score+=10# adding 10 we the snake collide with the food .

        delay-=0.001#changing the delay .

        # updating the highest score :-
        if score>highestscore:
            highestscore=score
        sb.clear()#here we clear the score_board window and write the new score and highest score
        sb.write("Score:() highestscore :{}".format(score,highestscore))

    # to move the snake body :-
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)

    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()

    # checking the collision with the snake body :-
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            for body in bodies:
               body.ht()
             #   pass
            #s.clear()
            bodies.clear()

            score=0
            delay=0.1

            sb.clear()
            sb.write("score:{} heghest score:{}".format(score,highestscore))
    time.sleep(delay)
#s.mainloop()

