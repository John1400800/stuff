import turtle as t


k = 20
t.color('black', 'red')
t.speed(0)
t.seth(90)

t.begin_fill()
for _ in range(2):
    t.fd(8*k)
    t.rt(90)
    t.fd(8*k)
    t.rt(90)
t.end_fill()

canvas = t.getcanvas()
t.tracer(0)
t.up()
cnt = 0
for y in range(-5*k, 10*k, k):
    for x in range(-5*k, 15*k, k):
        t.goto(x, y)
        if canvas.find_overlapping(x, -y, x, -y):
            t.dot(5, 'blue')
            cnt += 1
        else:
            t.dot(3, 'gray')


print(cnt)
t.done()
