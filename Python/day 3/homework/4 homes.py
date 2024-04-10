from turtle import *
import turtle


speed(19090)
width(7)
bgcolor("green")

#ca
penup()
goto(-1200, -100)
pendown()
color("deepskyblue")
begin_fill()
for i in range(2):
    forward(12100)
    left(90)
    forward(700)
    left(90)
end_fill()

#mze
penup()
goto(-320, 225)
pendown()
color("yellow")
begin_fill()
circle(35)
end_fill()

penup()
goto(-400, -200)
pendown()
color("brown")
begin_fill()
#xazi1
forward(150)
# xazi2
left(90)
forward(150)
# xazi3
left(90)
forward(150)
# xazi4
left(90)
forward(150)
end_fill()
# xazi5

left(90)
forward(55)
#karebi
begin_fill()
color("black")
# xazi6
left(90)
forward(75)
# xazi7
right(90)
forward(35)
# xazi8
right(90)
forward(75)
end_fill()
#saxuravi
penup()
goto(-250, -50)
pendown()

color("red")
begin_fill()
right(150)
forward(150)

left(120)
forward(150)
end_fill()

#xazi8
color("brown")
left(28)
forward(35)

left(90)
forward(25)

#windows
color("black")
right(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(12)
left(90)
forward(25)
left(90)
forward(12)
left(90)
forward(12)
left(90)
forward(25)






#SAXLI2
penup()
goto(-200, -200)
pendown()

color("brown")
begin_fill()
left(92)

#xazi1
forward(150)
# xazi2
left(90)
forward(150)
# xazi3
left(90)
forward(150)
# xazi4
left(90)
forward(150)
end_fill()
# xazi5

left(90)
forward(55)
#karebi
begin_fill()
color("black")
# xazi6
left(90)
forward(75)
# xazi7
right(90)
forward(35)
# xazi8
right(90)
forward(75)
end_fill()

#saxuravi
penup()
goto(-50, -50)
pendown()

color("red")
begin_fill()
right(150)
forward(150)

left(120)
forward(150)
end_fill()

#xazi8
color("brown")
left(28)
forward(35)

left(90)
forward(25)


#windows
color("black")
right(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(12)
left(90)
forward(25)
left(90)
forward(12)
left(90)
forward(12)
left(90)
forward(25)



#SAXLI3
penup()
goto(0, -200)
pendown()

color("brown")
begin_fill()
left(92)

#xazi1
forward(150)
# xazi2
left(90)
forward(150)
# xazi3
left(90)
forward(150)
# xazi4
left(90)
forward(150)
end_fill()
# xazi5

left(90)
forward(55)
#karebi
begin_fill()
color("black")
# xazi6
left(90)
forward(75)
# xazi7
right(90)
forward(35)
# xazi8
right(90)
forward(75)
end_fill()

#saxuravi
penup()
goto(150, -50)
pendown()

color("red")
begin_fill()
right(150)
forward(150)

left(120)
forward(150)
end_fill()

#xazi8
color("brown")
left(28)
forward(35)

left(90)
forward(25)

#windows
color("black")
right(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(12)
left(90)
forward(25)
left(90)
forward(12)
left(90)
forward(12)
left(90)
forward(25)


#SAXLI3
penup()
goto(200, -200)
pendown()

color("brown")
begin_fill()
left(92)

#xazi1
forward(150)
# xazi2
left(90)
forward(150)
# xazi3
left(90)
forward(150)
# xazi4
left(90)
forward(150)
end_fill()
# xazi5

left(90)
forward(55)
#karebi
begin_fill()
color("black")
# xazi6
left(90)
forward(75)
# xazi7
right(90)
forward(35)
# xazi8
right(90)
forward(75)
end_fill()

#saxuravi
penup()
goto(350, -50)
pendown()

color("red")
begin_fill()
right(150)
forward(150)

left(120)
forward(150)
end_fill()

#xazi8
color("brown")
left(28)
forward(35)

left(90)
forward(25)

#windows
color("black")
right(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(12)
left(90)
forward(25)
left(90)
forward(12)
left(90)
forward(12)
left(90)
forward(25)


def tree():

    color("saddlebrown")
    begin_fill()
    for i in range(2):
        forward(40)
        left(90)
        forward(10)
        left(90)
    end_fill()
    

    forward(10)
    left(90)
    forward(5)

    color("forestgreen")
    begin_fill()
    circle(25)
    end_fill()
    
    right(90)


penup()
goto(-25,-200)
pendown()
tree()
    

penup()
goto(200, -350)
pendown()
tree()


penup()
goto(300,-250)
pendown()
tree()


penup()
goto(-300,-250)
pendown()
tree()


penup()
goto(-200,-300)
pendown()
tree()
exitonclick()