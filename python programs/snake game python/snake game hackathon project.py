# importing the modules
import turtle# turtle module enables us to create pictures and shapes on the virtural canvas(screen).
import random# for random values
import time

#snakebody
bodies=[]

#getting a screen : canvas
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=500,height=500)

#create snake head
head=turtle.Turtle()
head.speed(0)# ['fastest’ :  0]  ,  [‘fast’    :  10]  ,  [‘normal’  :  6]  ,  [‘slow’    :  3]  ,  [‘slowest’ :  1]
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction="stop"#here we have taken a variable(attribute) 'direction' whose value we have given is 'stop' which represents the movement of  the head.

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.penup()# penup( ){picks up turtle's pen} :- basically makes sure that the moving object that we have created does not draw anything on the window.
food.goto(0,200)

# obstacles
obs=turtle.Turtle()
obs.speed(0)
obs.shape("square")
obs.color("blue")
obs.penup()
obs.goto(0,-100)

obs1=turtle.Turtle()
obs1.speed(0)
obs1.shape("square")
obs1.color("blue")
obs1.penup()
obs1.goto(-20,-100)

obs2=turtle.Turtle()
obs2.speed(0)
obs2.shape("square")
obs2.color("blue")
obs2.penup()
obs2.goto(80,-100)

obs3=turtle.Turtle()
obs3.speed(0)
obs3.shape("square")
obs3.color("blue")
obs3.penup()
obs3.goto(-40,-100)

obs4=turtle.Turtle()
obs4.speed(0)
obs4.shape("square")
obs4.color("blue")
obs4.penup()
obs4.goto(60,-100)

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

# key mappings
s.listen()
s.onkey(moveright,"Right")#onkey( ) function is used to map  the keys according to the keys pressed => syntax-> s.onkey( function_name , signature_of_the_key ) .
s.onkey(moveleft,"Left")#Left , Up ,Down , space , Right , d ,a ,s ,w are the key symbols .
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(movestop,"space")
s.onkey(moveright,"d")
s.onkey(moveleft,"a")
s.onkey(movedown,"s")
s.onkey(moveup,"w")

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
        x2=random.randint(-240,-65)
        x1=random.randint(65,240)
        y2=random.randint(-240,-220)
        y1=random.randint(-190,240)
        lx=[x1,x2]
        ly=[y1,y2]
        x=random.choice(lx)
        y=random.choice(ly)
        food.goto(x,y)
        # to increase the length of the snake.
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("green")
        bodies.append(body)#we are adding the body to the bodies(list) .
        
    # to move the snake body (except the nearest body part of the head):-
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)

    if len(bodies)>0:#for movement of the 1st element of the bodies list .
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()#for the movement of the head.
    
    # checking the collision with the snake body :-
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            for body in bodies:
               body.ht()
            bodies.clear()

    #checking the collision with obstacle :-
    if obs.distance(head)<20 or obs1.distance(head)<20 or obs2.distance(head)<20 or obs3.distance(head)<20 or obs4.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            for body in bodies:
               body.ht()
            bodies.clear()

    time.sleep(0.099)
