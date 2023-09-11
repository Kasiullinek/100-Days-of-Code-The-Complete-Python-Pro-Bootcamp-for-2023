from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score


game_is_over = False

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.turn_north)
screen.onkey(key="Down", fun=snake.turn_south)
screen.onkey(key="Left", fun=snake.turn_west)
screen.onkey(key="Right", fun=snake.turn_east)

while not game_is_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.respawn()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_over = True
        scoreboard.game_over()

    # Detect collision with head.
    for body_part in snake.body[1:]:
        if snake.head.distance(body_part) < 15:
            game_is_over = True
            scoreboard.game_over()

screen.exitonclick()
