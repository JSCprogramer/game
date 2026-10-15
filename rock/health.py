import turtle as t
from . import rock

bar_turtle = t.Turtle()
bar_turtle.hideturtle()
bar_turtle.penup()
bar_turtle.speed(0)

def update_bar():
    bar_turtle.clear()

    # Rock's top-left corner
    x = rock.rock_turtle.xcor()
    y = rock.rock_turtle.ycor()

    # Position bar directly under rock
    bar_x = x
    bar_y = y - 110  # 100px rock height + 10px spacing

    # Draw red background (full bar)
    bar_turtle.goto(bar_x, bar_y)
    bar_turtle.color("red")
    bar_turtle.begin_fill()
    for _ in range(2):
        bar_turtle.forward(100)
        bar_turtle.left(90)
        bar_turtle.forward(10)
        bar_turtle.left(90)
    bar_turtle.end_fill()

    # Draw green health amount
    bar_turtle.goto(bar_x, bar_y)
    bar_turtle.color("green")
    bar_turtle.begin_fill()
    width = rock.hp  # health value
    for _ in range(2):
        bar_turtle.forward(width)
        bar_turtle.left(90)
        bar_turtle.forward(10)
        bar_turtle.left(90)
    bar_turtle.end_fill()
