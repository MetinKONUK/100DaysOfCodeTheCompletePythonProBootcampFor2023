from turtle import Turtle, Screen


def dashed(pen: Turtle, space: float, length: float) -> None:
    """Draw dashed line with turtle."""
    pen.forward(length)
    pen.penup()
    pen.forward(space)
    pen.pendown()


def main() -> None:
    pen = Turtle()
    pen.shape("turtle")
    for _ in range(10):
        dashed(pen, 5, 10)
    screen = Screen()
    screen.exitonclick()


main()

