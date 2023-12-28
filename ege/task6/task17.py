from turtle import *

def go(x, y):
    global k
    goto(xcor()+x*k, ycor()+y*k)

k = 20
screensize(100*k, 100*k)
ht()
seth(90)
speed(0)
color('black', 'red')

up()
go(5, 5)
down()
begin_fill()
# S1=5*5*0.5=12.5
# 19*12.5=237.5 --> 237
for _ in range(20):
    go(-5, -5)
    go( 0,  5)
go(0, -5)
for _ in range(20):
    go(5, 0)
end_fill()

canvas = getcanvas()

up()
tracer(0)
cnt = 0
for y in range(-20*k, 30*k, k):
    for x in range(-20*k, 20*k, k):
        goto(x, y)
        if canvas.find_overlapping(x, -y, x, -y)==(5,):
            dot(5, 'blue')
            cnt += 1
        else:
            dot(4, 'yellow')

print(cnt)
done()
