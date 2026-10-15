import turtle as t
from . import rock

bar_turtle = t.Turtle()
bar_turtle.hideturtle()
bar_turtle.penup()
bar_turtle.speed(0)

def update_bar():
    

    # Position bar under the rock
    x = rock.rock_turtle.xcor()
    y = rock.rock_turtle.ycor() - 20  # 20 pixels below rock

    bar_turtle.goto(x - 50, y)  # left side of bar

    # Background (red)
    bar_turtle.color("red")
    bar_turtle.begin_fill()
    for _ in range(2):
        bar_turtle.forward(100)
        bar_turtle.left(90)
        bar_turtle.forward(10)
        bar_turtle.left(90)
    bar_turtle.end_fill()

    # Health amount (green)
    bar_turtle.goto(x - 50, y)
    bar_turtle.color("green")
    bar_turtle.begin_fill()
    
    width = rock.health  # health controls bar length
    for _ in range(2):
        bar_turtle.forward(width)
        bar_turtle.left(90)
        bar_turtle.forward(10)
        bar_turtle.left(90)
    bar_turtle.end_fill()
