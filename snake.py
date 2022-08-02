from turtle import Turtle

STARTING_POSITIONS: list = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE: float = 20
UP: float = 90
DOWN: float = 270
LEFT: float = 180
RIGHT: float = 0


class Snake:
    def __init__(self) -> None:
        self.segments: list = []
        self.create_snake()
        self.head: Turtle = self.segments[0]

    def create_snake(self) -> None:
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self) -> None:
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_segment)