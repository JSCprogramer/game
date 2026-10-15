import turtle as t
from . import health

rock_turtle = t.Turtle()
rock_turtle.fillcolor("grey")
rock_turtle.hideturtle()
rock_turtle.penup()
rock_turtle.speed(0)

hp = 100  # rock health

def draw_rock():
    # rock_turtle position = CENTER of the rock
    cx = rock_turtle.xcor()
    cy = rock_turtle.ycor()

    # Convert center → bottom-left corner
    bl_x = cx - 50
    bl_y = cy - 50

    # Draw rock from bottom-left
    rock_turtle.goto(bl_x, bl_y)
    rock_turtle.showturtle()
    rock_turtle.begin_fill()
    rock_turtle.pendown()
    for _ in range(4):
        rock_turtle.forward(100)
        rock_turtle.left(90)
    rock_turtle.end_fill()
    rock_turtle.penup()
    rock_turtle.hideturtle()

    # Return turtle to center
    rock_turtle.goto(cx, cy)

    health.update_bar()
