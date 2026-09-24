import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("3D Cube")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(3)

# Cube points
points = [
    (-100, -100),
    (100, -100),
    (100, 100),
    (-100, 100),
    (-100, -100)
]

# Front square
t.color("cyan")
t.penup()
t.goto(points[0])
t.pendown()

for point in points[1:]:
    t.goto(point)

# Back square
t.color("magenta")
t.penup()
t.goto(-50, -50)
t.pendown()

back_points = [
    (-50, -50),
    (150, -50),
    (150, 150),
    (-50, 150),
    (-50, -50)
]

for point in back_points[1:]:
    t.goto(point)

# Connecting lines
t.color("yellow")

connections = [
    ((-100, -100), (-50, -50)),
    ((100, -100), (150, -50)),
    ((100, 100), (150, 150)),
    ((-100, 100), (-50, 150))
]

for start, end in connections:
    t.penup()
    t.goto(start)
    t.pendown()
    t.goto(end)

turtle.done()