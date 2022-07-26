from turtle import Turtle, Screen
from random import choice


def color_picker():
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
               "SeaGreen"]
    return choice(colours)


def shape(pen: Turtle, n: int):
    """Draws a regular shape with n sides."""
    pen.color(color_picker())
    for _ in range(n):
        pen.forward(100)
        pen.rt(360 // n)


def main() -> None:
    pen = Turtle()
    pen.shape("turtle")
    for n in range(3, 10):
        shape(pen, n)
    screen = Screen()
    screen.exitonclick()


main()
