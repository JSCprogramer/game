import turtle as t
from . import rock

bar_turtle = t.Turtle()
bar_turtle.hideturtle()
bar_turtle.penup()
bar_turtle.speed(0)

def update_bar():
    bar_turtle.clear()

    # Rock center
    cx = rock.rock_turtle.xcor()
    cy = rock.rock_turtle.ycor()

    # Bottom-left corner of rock
    bl_x = cx - 50
    bl_y = cy - 50

    # Bar position (15px below rock)
    bar_x = bl_x
    bar_y = bl_y - 15

    # Red background (full bar)
    bar_turtle.goto(bar_x, bar_y)
    bar_turtle.color("red")
    bar_turtle.begin_fill()
    for _ in range(2):
        bar_turtle.forward(100)
        bar_turtle.left(90)
        bar_turtle.forward(10)
        bar_turtle.left(90)
    bar_turtle.end_fill()

    # Green health amount
    bar_turtle.goto(bar_x, bar_y)
    bar_turtle.color("green")
    bar_turtle.begin_fill()
    width = rock.hp  # health value (0–100)
    for _ in range(2):
        bar_turtle.forward(width)
        bar_turtle.left(90)
        bar_turtle.forward(10)
        bar_turtle.left(90)
    bar_turtle.end_fill()
