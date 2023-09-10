from turtle import Screen
import time
from snake import Snake


game_is_over = False

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()

screen.onkey(key="Up", fun=snake.turn_north)
screen.onkey(key="Down", fun=snake.turn_south)
screen.onkey(key="Left", fun=snake.turn_west)
screen.onkey(key="Right", fun=snake.turn_east)

while not game_is_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
