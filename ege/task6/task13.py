import turtle as t


k = 20
t.speed(0)
t.color('black', 'red')
t.seth(90)

t.begin_fill()
for _ in range(2):
    t.fd(9*k)
    t.rt(90)
    t.fd(2*k)
    t.rt(90)
t.end_fill()
canvas = t.getcanvas()

t.up()
t.tracer(0)
cnt = 0
for y in range(-2*k, 11*k, k):
    for x in range(-5*k, 5*k, k):
        t.goto(x, y)
        if {4, 5}.isdisjoint(set(canvas.find_overlapping(x, -y, x, -y))):
            t.dot(3, 'gray')
        else:
            t.dot(5, 'blue')
            cnt += 1

print(cnt)
t.done()
