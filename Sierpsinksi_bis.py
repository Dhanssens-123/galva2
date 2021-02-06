import turtle
import math

def triangle(len, a, b):
    turtle.up()
    turtle.goto(a - len/2, b - len/3)
    turtle.down()
    for i in range(3):
        turtle.forward(len)
        turtle.left(120)

def sierpinski(n, len, a=0, b=0):
    if n > 0:
        sierpinski(n - 1, len / 2, a - len / 4, b - math.sqrt(3)*len/6 + math.sqrt(3)/12*len)
        sierpinski(n - 1, len / 2, a + len/4,  b - math.sqrt(3)*len/6 + math.sqrt(3)/12*len)
        sierpinski(n - 1, len / 2, a, b + 1/3 * math.sqrt(3)/2 * len)
        triangle(len, a, b)

turtle.tracer(0)
sierpinski(3,600)
turtle.done()