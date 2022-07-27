from turtle import Turtle, Screen, colormode
from random import choice
from colorgram import extract


def extract_colors(path: str, kind: int) -> list:
    colors: list = extract(path, 100)
    return [tuple(color.rgb) if kind == 0 else tuple(color.hsl) for color in colors][2:]


def painting(pen: Turtle, colors: list) -> None:
    pen.setheading(225)
    pen.forward(325)
    pen.setheading(0)
    for __ in range(10):
        for _ in range(10):
            pen.dot(30, choice(colors))
            pen.forward(50)
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)
        pen.forward(500)
        pen.setheading(0)
    pen.hideturtle()


def main() -> None:
    pen = Turtle()
    pen.speed("fastest")
    pen.penup()

    colormode(255)
    colors = extract_colors("image.jpg", 0)
    painting(pen, colors)
    screen = Screen()
    screen.exitonclick()


main()
