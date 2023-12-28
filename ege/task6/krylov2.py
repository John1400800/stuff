import turtle

m = 16
turtle.left(90)
turtle.speed(0)

for i in range(7):
    turtle.forward(10*m)
    turtle.right(120)

turtle.up()
for x in range(0, 10):
    for y in range(0, 11):
        turtle.goto(x*m, y*m)
        turtle.dot(4)

turtle.done()
