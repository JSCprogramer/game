import turtle as t
from ui import base_bg
from rock import rock
from rock import health
base_bg.setup_bg()

# Move rock anywhere you want
rock.rock_turtle.goto(0, 75)
rock.draw_rock()

t.done()