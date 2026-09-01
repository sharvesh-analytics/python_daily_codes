import turtle

t = turtle.Turtle()
t.speed(0)

for i in range(60):
    t.circle(i * 2)
    t.right(10)

turtle.done()