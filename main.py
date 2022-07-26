from turtle import Turtle, Screen


def fr(pen: Turtle, distance, angle):
    pen.forward(distance)
    pen.rt(angle)


def main():
    pen = Turtle()
    pen.shape("turtle")
    for _ in range(4):
        fr(pen, 100, 90)
    screen = Screen()
    screen.exitonclick()


main()

