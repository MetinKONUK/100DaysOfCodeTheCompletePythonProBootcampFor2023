from turtle import Turtle, Screen, colormode
from random import random, choice, randint
global winner


def draw_finish_line(pen: Turtle):
    pen.penup()
    pen.goto(200, 500)
    pen.pendown()
    pen.goto(200, -500)
    pen.hideturtle()


def start_position(racer: Turtle, x: float, y: float) -> None:
    racer.speed("slow")
    racer.setposition(x, y)
    racer.speed("slowest")


def appearance(racer: Turtle, color: str):
    racer.penup()
    racer.shape("turtle")
    racer.shapesize(2, 2, 1)
    racer.color(color)


def create_racers() -> list:
    colors: list = ["red", "green", "blue", "yellow", "pink"]
    racers: list = []
    position: float = 120
    color_index = 0
    for _ in range(5):
        racer = Turtle()
        racer.speed("slowest")
        appearance(racer, colors[color_index])
        color_index += 1
        start_position(racer, -250, position)
        position -= 60
        racers.append(racer)
    return racers


def check_winner(racers: list) -> bool:
    for racer in racers:
        if racer.xcor() >= 200:
            global winner
            winner = racer.color()
            return False
    return True


def race(racers: list):
    while check_winner(racers):
        for racer in racers:
            racer.forward(randint(15, 30))


def main() -> None:
    screen = Screen()
    screen.setup(width=600, height=400)
    draw_finish_line(Turtle())
    racers = create_racers()
    guess = screen.textinput(title="Make your bet!", prompt="Which turtle do you support?: Enter a colour: ").lower()
    race(racers)
    print("Correct!" if winner[0] == guess else "Wrong!", f"{winner[0].capitalize()} is the winner!")
    screen.exitonclick()


main()
