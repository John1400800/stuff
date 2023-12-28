import turtle as t


k = 100
t.hideturtle()
t.screensize(220*k, 220*k)
t.seth(90)
t.speed(0)
t.color('black', 'red')

t.begin_fill()
for _ in range(3):
    t.fd(111*k)
    t.rt(120)
t.end_fill()

canvas = t.getcanvas()

t.up()
t.tracer(0)
cnt = 0
for y in range(-k, 115*k, k):
    for x in range(-k, 100*k, k):
        t.goto(x, y)
        if canvas.find_overlapping(x, -y, x, -y)==(5,):
            t.dot(5, 'blue')
            cnt += 1
        else:
            t.dot(3, 'gray')

print(cnt)
t.done()
