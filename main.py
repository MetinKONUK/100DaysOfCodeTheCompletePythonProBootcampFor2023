from turtle import Turtle, Screen
from random import choice


def color_picker() -> str:
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
               "SeaGreen"]
    return choice(colours)


def spirograph(pen: Turtle, offset: int, radius: float):
    pen.speed("fastest")
    circle_count = 360 // offset
    for _ in range(circle_count):
        pen.color(color_picker())
        pen.circle(radius)
        pen.setheading(pen.heading() + offset)


def main() -> None:
    pen = Turtle()
    spirograph(pen, 5, 100)
    screen = Screen()
    screen.exitonclick()


main()
