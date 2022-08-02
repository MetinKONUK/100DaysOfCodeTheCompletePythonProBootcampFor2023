from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="Snake Game")
screen.tracer(n=0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")

game_is_on: bool = True

while game_is_on:
    screen.update()
    sleep(0.05)
    snake.move()
    if snake.head.distance(food) < 20:
        food.create_food()
        snake.add_segment()
screen.exitonclick()
