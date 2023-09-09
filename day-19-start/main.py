from turtle import Turtle, Screen

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

def etch_a_sketch():
    screen.listen()
    screen.onkeypress(key="w", fun=move_forward)
    screen.onkeypress(key="s", fun=move_backwards)
    screen.onkeypress(key="a", fun=move_counter_clockwise)
    screen.onkeypress(key="d", fun=move_clockwise)
    screen.onkey(key="c", fun=clear_drawing)

sam = Turtle()
screen = Screen()

etch_a_sketch()

screen.exitonclick()