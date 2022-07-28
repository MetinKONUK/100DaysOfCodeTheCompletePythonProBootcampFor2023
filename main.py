from turtle import Turtle, Screen, colormode
from functools import partial
from random import choice
from colorgram import extract
index: int = 0


def clear_screen(pen: Turtle) -> None:
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()


def switch_color(pen: Turtle, colors: list) -> None:
    global index
    pen.color(colors[index % 4])
    index += 1


def main() -> None:
    pen = Turtle()

    colors: list = ["red", "green", "blue", "black"]

    screen = Screen()

    screen.onkey(partial(pen.forward, 10), 'w')
    screen.onkey(partial(pen.rt, 10), 'd')
    screen.onkey(partial(pen.back, 10), 's')
    screen.onkey(partial(pen.lt, 10), 'a')

    screen.onkey(partial(clear_screen, pen), 'c')

    screen.onkey(partial(switch_color, pen, colors), "space")

    screen.listen()
    screen.exitonclick()


main()
