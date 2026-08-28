import turtle

t = turtle.Turtle()
t.speed(0)

for i in range(50):
    t.forward(i * 5)
    t.right(90)

turtle.done()