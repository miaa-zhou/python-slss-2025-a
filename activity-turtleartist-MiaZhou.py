# Turtle Artist
# Author: Mia Zhou
# 28 October

import turtle


# Create a dictionary of colours
colors = {
    "lavender pink": "#eeabc4",
    "tea green": "#c1d7ae",
    "outer space": "#495159",
    "mindaro": "#feffa5",
    "sunset": "#ffd289",
    "powder blue": "#aec5eb",
}

# One of a kind turtle
wn = turtle.Screen()
wn.bgcolor("powder blue")

t = turtle.Turtle()

# Creating the turtle
t = turtle.Turtle()
t.pensize(5)
t.speed(1)
wn = turtle.Screen()


# Helper function to draw a rectangle
def draw_rectangle(width, height, color_name):
    t.color(color_name)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.right(90)
    t.end_fill()


# Helper function to draw a tower
def draw_tower(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    draw_rectangle(50, 150, colors["lavender pink"])


# Drawing the tower battlements
t.color(colors["tea green"])
for i in range(3):
    t.begin_fill()
    for _ in range(4):
        t.forward(15)
        t.right(90)
    t.end_fill()
    t.forward(17)

# Drawing the base of the castle
t.penup()
t.goto(-100, -100)
t.pendown()
draw_rectangle(200, 100, colors["outer space"])

# Drawing the left and right towers
# draw_tower(-150, 0)
# draw_tower(100, 0)

# Drawing the door
# t.penup()
# t.goto(-25, -100)
# t.pendown
# t.color(colors["sunset"])
# t.begin_fill()
# for _ in range(2):
#     t.forward(50)
#     t.left(90)
#     t.forward(70)
#     t.right(90)
# t.end_fill()

# Drawing the sun
t.penup()
t.goto(150, 150)
t.pendown()
t.color(colors["mindaro"])
t.begin_fill()
t.circle(35)
t.end_fill()

wn.exitonclick()
