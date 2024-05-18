from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(50)


def move_backward():
    tim.back(50)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(move_backward, "s")
screen.onkey(clear, "c")
screen.exitonclick()
