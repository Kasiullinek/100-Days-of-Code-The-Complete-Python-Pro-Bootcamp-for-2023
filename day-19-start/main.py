from turtle import Turtle, Screen
import random

def etch_a_sketch():
    def move_forward():
        sam.forward(10)

    def move_backwards():
        sam.back(10)

    def move_counter_clockwise():
        sam.left(10)

    def move_clockwise():
        sam.right(10)

    def clear_drawing():
        sam.clear()
        sam.penup()
        sam.home()
        sam.pendown()

    sam = Turtle()
    screen.listen()

    screen.onkeypress(key="w", fun=move_forward)
    screen.onkeypress(key="s", fun=move_backwards)
    screen.onkeypress(key="a", fun=move_counter_clockwise)
    screen.onkeypress(key="d", fun=move_clockwise)
    screen.onkey(key="c", fun=clear_drawing)

def turtle_race():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_position = [-100, -60, -20, 20, 60, 100]
    is_race_on = False
    all_turtles = []

    screen.setup(500, 400)
    user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

    for turtle_index in range(0,6):
        julia = Turtle("turtle")
        julia.color(colors[turtle_index])
        julia.penup()
        julia.goto(-230, y_position[turtle_index])
        all_turtles.append(julia)

    if user_bet:
        is_race_on = True

    while is_race_on:

        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")

            random_speed = random.randint(0,10)
            turtle.forward(random_speed)


screen = Screen()

etch_a_sketch()
# turtle_race()

screen.exitonclick()