import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed(0)


def draw_spirograph():
    for i in range(0, 361, 5):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(i)


draw_spirograph()
screen = Screen()
screen.exitonclick()
