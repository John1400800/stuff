import turtle as t


k = 10
t.seth(90)
t.speed(0)
t.color('black', 'red')

t.begin_fill()
t.rt(180)
t.fd(2*k)
t.rt(90)
t.fd(30*k)
t.rt(90)
t.fd(2*k)
t.rt(30)
for _ in range(6):
    t.fd(5*k)
    t.rt(120)
    t.fd(5*k)
    t.rt(240)
t.end_fill()

canvas = t.getcanvas()

t.up()
t.tracer(0)
cnt = 0
for y in range(-10*k, 10*k, k):
    for x in range(-40*k, 10*k, k):
        t.goto(x, y)
        if canvas.find_overlapping(x, -y, x, -y) ==(5,):
            t.dot(5, 'blue')
            cnt += 1
        else:
            t.dot(3, 'gray')

print(cnt)
t.done()


