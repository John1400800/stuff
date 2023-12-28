from turtle import *


k = 20
screensize(100*k, 100*k)
seth(90)
speed(0)
color('black', 'red')
ht()

begin_fill()
for _ in range(8):
    fd(10*k)
    rt(45)
end_fill()

canvas = getcanvas()

up()
tracer(0)
cnt = 0
for y in range(-10*k, 20*k, k):
    for x in range(-10*k, 40*k, k):
        goto(x, y)
        if canvas.find_overlapping(x, -y, x, -y) and canvas.find_overlapping(x, -y, x, -y)!=(5,):
            dot(5, 'blue')
            cnt += 1
print(cnt)
