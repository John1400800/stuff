import turtle

m = 20
turtle.speed(0)
turtle.color("black", "red")
turtle.hideturtle()

turtle.tracer(0)
turtle.up()
turtle.right(180)
turtle.forward(14*m)
turtle.right(90)
turtle.pd()

turtle.begin_fill()
turtle.right(60)
for _ in range(4):
    turtle.forward(8*m)
    turtle.right(120)
    turtle.forward(4*m)
    turtle.right(240)
turtle.right(120)
turtle.forward(2*m)
turtle.right(90)
turtle.forward(16*3**0.5*m)
turtle.right(90)
turtle.forward(2*m)
turtle.end_fill()

c = 0
canvas = turtle.getcanvas()
print(type(canvas), canvas.__class__.__mro__)
turtle.penup()
for y in range(-20*m, 20*m, m):
    for x in range(-20*m, 20*m, m):
        if canvas.find_overlapping(x, -y, x, -y) == (5,):
            c += 1
            turtle.goto(x,y)
            turtle.dot(5, 'blue')
        else:
            turtle.goto(x,y)
            turtle.dot(3, 'gray')
 
print(c)
turtle.done()
