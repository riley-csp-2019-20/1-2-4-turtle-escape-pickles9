import turtle as turtle 
import random 
import time
bob = turtle.Turtle()#makes maze drawer
wn = turtle.Screen() #makes screen variable
bob.ht() 
bob.speed(0) #gives bob meth
num_of_walls = 46 #adjusts the number of walls
wall_angle = 90 #adjusts wall angle
wall_spaceing = 15 #changes number that is added to the length each loop
count=0 #creates counter variable
#Changes colors
bob.pencolor("red")
bob.pensize(5)
wn.bgcolor("black")
#makes maze runner
runner = turtle.Turtle() 
runner.speed(0)
runner.color("green")
#makes screen variable
wn = turtle.Screen()
#sets up movement controls for maze runner
def up():
    runner.forward(10)
    victory_check()
def right():
    runner.right(90)
    victory_check()
def down():
    runner.forward(-10)
    victory_check()
def left():
    runner.left(90)
    victory_check()
#checks for victory contition
def victory_check():
    if((runner.xcor()<-350)or(runner.xcor()>370)or(runner.ycor()<-340)or(runner.ycor()>340)):
        bob.clear()
        bob.pu()
        runner.ht()
        runner.pu()
        runner.clear()
        bob.color("white")
        bob.goto(0,100)
        bob.write("You Win!", align="center", font=("Arial", 100, "normal"))
        while(True):
            wn.bgcolor("red")
            time.sleep(1/120)
            wn.bgcolor("green")
            time.sleep(1/120)
            wn.bgcolor("blue")
            time.sleep(1/120)

while count < num_of_walls:  #loop that draws maze
    total_length = (25 + (count * wall_spaceing))-20
    if (total_length < 80): #if statement prevents negative nubers
        bob.forward(25 + (count * wall_spaceing))
        bob.right(wall_angle)
    else:
        random_length = random.randint(wall_spaceing*2, total_length - (wall_spaceing*2)) #saves random length as a variable
        bob.forward(random_length) #travels random length
        bob.pu() #draws gap
        bob.forward(20)
        bob.pd()
        bob.right(wall_angle) #draw perpendicular barrier
        bob.forward(wall_spaceing*2)
        bob.backward(wall_spaceing*2)
        bob.left(wall_angle)
        bob.forward(total_length - random_length) #continues rest of way
        bob.right(wall_angle)
    count += 1 #adds one to the counter
#controls for maze runner
wn.onkeypress(up, "Up")
wn.onkeyrelease(right,"Right")
wn.onkeypress(down,"Down")
wn.onkeyrelease(left,"Left")
wn.listen() 
wn.mainloop()