from turtle import Turtle, Screen
from random import choice


def color_picker() -> str:
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
               "SeaGreen"]
    return choice(colours)


def random_walk(pen: Turtle, directions: list, distance: float, width: int, speed: str, cycles: int) -> None:
    pen.pensize(width)
    pen.speed(speed)
    while cycles:
        pen.color(color_picker())
        pen.setheading(choice(directions))
        pen.forward(distance)
        cycles -= 1


def main() -> None:
    pen = Turtle()
    directions = [0, 90, 180, 270]
    random_walk(pen, directions, 10, 4, "fastest", 200)
    screen = Screen()
    screen.exitonclick()


main()
