from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-150
y1 =75
x2 =-100
y2 =250
x3 =-150
y3 =-150
x4 =-150
y4 =-250


#Section 2 - Setup
#TODO - use your own background, and set your four turtles to images of your choice
set_background("hawaii")
t1 = create_sprite("junko",x1,y1)
t2 = create_sprite("turtle3",x2,y2)
t3 = create_sprite("cardinal",x3,y3)
t4 = create_sprite("dog",x4,y4)


#Section 3 - Racing
##ODO - explain here which sprites are faster or slower
for i in range(50):
    x1 +=5
    x2 +=10
    x3 +=8
    x4 +=9

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


#Section 4 - Winner
#TODO - complete the elif for player 2 winning
#TODO - write another elif for player 3 and player 4
s5 = create_sprite("alien",-200,-200)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
     s5.write("Player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    s5.write("player 2 wins!")


turtle.exitonclick()
#sprite2 is the fastest the turtle