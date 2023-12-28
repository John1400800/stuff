import turtle as t


k = 10
t.color('black', 'red')
t.speed(0)
t.seth(90)

t.begin_fill()
t.rt(180)
t.fd(2*k)
t.rt(90)
t.fd(40*k)
t.rt(90)
t.fd(2*k)
for _ in range(4):
    t.seth(90)
    t.circle(-5*k, 180)
t.end_fill()

canvas = t.getcanvas()

t.up()
t.tracer(0)
cnt = 0
for y in range(-12*k, 15*k, k):
    for x in range(-40*k, 15*k, k):
        t.goto(x, y)
        if canvas.find_overlapping(x, -y, x, -y) == (5,):
            t.dot(5, 'blue')
            cnt += 1
        else:
            t.dot(3, 'gray')
print(cnt)
t.mainloop()
