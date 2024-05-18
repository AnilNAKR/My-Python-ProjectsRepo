from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")


def draw_shape(num_sides, pencolor):
    angle = 360 // num_sides
    for _ in range(num_sides):
        tim.color(pencolor)
        tim.forward(100)
        tim.right(angle)


color_list = ["Navy", "Red", "DarkGreen", "Teal", "OrangeRed", "FireBrick", "Magenta", "Maroon"]
for sides in range(3, 11):
    draw_shape(sides, color_list[sides - 3])

screen = Screen()
screen.exitonclick()
