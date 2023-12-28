from turtle import *


k = 40
screensize(100*k, 100*k)
ht()
seth(90)
speed(0)
color('black', 'red')

begin_fill()
for _ in range(4):
    for _ in range(3):
        fd(6*k)
        lt(120)
    rt(120)
end_fill()

canvas = getcanvas()

up()
tracer(0)
cnt = 0
for y in range(-20*k, 20*k, k):
    for x in range(-20*k, 20*k, k):
        goto(x, y)
        if canvas.find_overlapping(x, -y, x, -y)==(5,):
            dot(5, 'blue')
            cnt += 1
        else:
            dot(4, 'yellow')

print(cnt)
done()
