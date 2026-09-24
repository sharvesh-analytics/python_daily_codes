import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)

colors = [
    "red", "orange", "yellow",
    "lime", "cyan", "blue",
    "magenta", "purple"
]

for i in range(72):

    t.color(colors[i % len(colors)])

    for j in range(4):
        t.forward(100)
        t.right(90)

    t.right(5)

turtle.done()