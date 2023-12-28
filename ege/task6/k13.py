import turtle as t


k = 100
t.seth(90)
t.speed(0)
t.color('black', 'red')

t.begin_fill()
t.rt(60)
for _ in range(4):
    t.fd(8*k)
    t.rt(120)
    t.fd(4*k)
    t.rt(240)
t.rt(120)
t.fd(2*k)
t.rt(90)
t.fd(16*3**0.5*k)
t.rt(90)
t.fd(2*k)
t.end_fill()

canvas = t.getcanvas()

t.up()
t.tracer(0)
cnt = 0
for y in range(-10*k, 20*k, k):
    for x in range(-20*k, 40*k, k):
        t.goto(x, y)
        if canvas.find_overlapping(x, -y, x, -y) == (5,):
            t.dot(5, 'blue')
            cnt += 1
        else:
            t.dot(3, 'gray')

print(cnt)
t.done()


