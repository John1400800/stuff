import turtle as t


k = 100
t.screensize(170*k, 10*k)
t.hideturtle()
t.seth(90)
t.speed(0)
t.color('black', 'red')

t.begin_fill()
t.rt(180)
t.fd(2*k)
t.rt(90)
t.fd(80*k)
t.rt(90)
t.fd(2*k)
for _ in range(8):
    t.circle(-5*k, 180)
    t.seth(90)
t.end_fill()

canvas = t.getcanvas()

t.up()
t.tracer(0)
cnt = 0
for y in range(-10*k, 10*k, k):
    for x in range(-90*k, 10*k, k):
        t.goto(x, y)
        if canvas.find_overlapping(x, -y, x, -y)==(5,):
            t.dot(5, 'blue')
            cnt += 1
        else:
            t.dot(3, 'gray')

print(cnt)
t.done()
