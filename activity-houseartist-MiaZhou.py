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
constructor = turtle.Turtle()
constructor.color("grey")
t = turtle.Turtle()
t.pensize(10)
t.speed(15)
wn = turtle.Screen()
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.speed(15)


# Draw the house
def draw_square(size: float):
    for _ in range(4):
        constructor.forward(size)
        constructor.left(90)


def draw_triangle(size: float):
    constructor.forward(size)
    constructor.left(135)
    constructor.forward(size / (2**0.5))
    constructor.left(90)
    constructor.forward(size / (2**0.5))
    constructor.left(135)


# Draw the house
constructor.fillcolor(colors["lavender pink"])
constructor.begin_fill()
draw_square(200)
constructor.end_fill()

# Draw the roof
constructor.fillcolor(colors["outer space"])
constructor.begin_fill()
constructor.left(90)
constructor.forward(200)
constructor.right(90)
draw_triangle(200)
constructor.end_fill()

# Draw the door
constructor.fillcolor(colors["sunset"])
constructor.penup()
constructor.goto(85, -200)
constructor.pendown()
constructor.begin_fill()
constructor.setheading(0)

# Draw the window
constructor.fillcolor(colors["tea green"])
constructor.right(90)
constructor.begin_fill()
constructor.forward(50)
constructor.left(90)
constructor.forward(50)
constructor.left(90)
constructor.forward(50)
constructor.end_fill()
constructor.left(90)
constructor.forward(100)
constructor.right(90)

# Draw the circle for the sun
sun.begin_fill()
sun.circle(50)
sun.end_fill()

# Draw the rays for the sun
for i in range(12):
    sun.penup()
    sun.goto(0, 0)
    sun.forward(50)
    sun.pendown()
    sun.forward(30)
    sun.penup()
    sun.goto(0, 0)
    sun.right(30)

# Hide the turtle and finish
constructor.hideturtle()
sun.hideturtle()
# Keep the window open
wn.exitonclick()
