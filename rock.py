import turtle as tut

tut.fillcolor("grey")
tut.hideturtle()


tut.penup()
tut.speed(0)

def rock():
    tut.begin_fill()
    tut.pendown()
    tut.forward(100)
    tut.left(90)
    tut.forward(100)
    tut.left(90)
    tut.forward(100)
    tut.left(90)
    tut.forward(100)
    tut.left(90)
    tut.end_fill()


rock()

