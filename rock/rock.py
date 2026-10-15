import turtle as t
from . import health


rock_turtle = t.Turtle()
rock_turtle.fillcolor("grey")
rock_turtle.hideturtle()
rock_turtle.penup()
rock_turtle.speed(0)

hp = 100

def draw_rock():
    rock_turtle.begin_fill()
    rock_turtle.pendown()
    for _ in range(4):
        rock_turtle.forward(100)
        rock_turtle.left(90)
    rock_turtle.end_fill()
    rock_turtle.penup()

    health.update_bar()

