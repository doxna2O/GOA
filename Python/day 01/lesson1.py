from turtle import *
import turtle
 
color("purple")
speed(10)
width(7)
#xazi 1
forward(200)
left(90)

#xazi 2
forward(200)
left(90)
 
#xazi 3
forward(200)
left(90)

#xazi 4
forward(200)
left(90)

#karebi
forward(70)
color("yellow")
begin_fill()
left(90)
 
forward(120)
right(90)

forward(60)
right(90)

forward(120)
end_fill()

#saxuravi
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

color("purple")
left(30)
forward(40)

color("purple")
left(90)
forward(7)

color("green")
forward(20)

color("brown")
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(15)
right(90)
forward(30)
right(90)
forward(15)
right(90)
forward(15)
right(90)
forward(30)

drawing_area = turtle.Screen()
drawing_area.title("Screen Demo")
drawing_area.bgcolor("green")
exitonclick()