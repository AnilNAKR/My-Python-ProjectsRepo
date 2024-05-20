from turtle import Turtle, Screen
import random
import turtle as t

tim = Turtle()
tim.shape("circle")
t.colormode(255)

# color_list = ["Navy", "Red", "DarkGreen", "Teal", "OrangeRed", "FireBrick", "Magenta", "Maroon"]
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(200):
    # tim.color(random.choice(color_list))
    tim.color(random_color())
    tim.speed(0)
    tim.pensize(15)
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
