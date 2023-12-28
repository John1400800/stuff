import turtle as t


k = 100
t.seth(90)
t.speed(0)
t.color('black', 'red')

t.rt(30)
t.begin_fill()
for _ in range(4):
    t.fd(25*k)
    t.rt(90)
t.end_fill()

canvas = t.getcanvas()

t.up()
t.tracer(0)
cnt = 0
for y in range(-30*k, 30*k, k):
    for x in range(-2*k, 40*k, k):
        t.goto(x, y)
        if canvas.find_overlapping(x, -y, x, -y) == (5,):
            t.dot(5, 'blue')
            cnt += 1
        else:
            t.dot(3, 'gray')

print(cnt)
t.done()
            



