from turtle import*

bgcolor("black")
speed(0)

penup()
goto(-200,0)
pendown()

for i in range(3) :
    for colorurs in ["red", "magenta", "blue", "green", "yellow", "white"] :
        color(colorurs)
        pensize(3)
        circle(150)
        forward(20) 