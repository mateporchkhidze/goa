from turtle import *

#at first create square.
speed(30)
width(5)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#make a door
forward(70)
color("red")
left(90)
forward(90)
right(90)
forward(50)
right(90)
forward(90)

#make a roof
color("blue")
penup()
goto(200,200)
pendown()
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#make first window
color("black")
penup()
goto(0,0)
pendown()
right(150)
forward(160)
right(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60) 

#make second window
penup()
goto(200,160)
pendown()
forward(60)
left(90)
forward(40)
left(90)
forward(60)


exitonclick()