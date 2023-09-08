import turtle
from turtle import Turtle, Screen
import random

def draw_a_square():
    for _ in range(4):
        sam.right(90)
        sam.forward(100)

def draw_a_dashed_line():
    for _ in range(50):
        sam.forward(5)
        sam.penup()
        sam.forward(5)
        sam.pendown()

def draw_shapes():
    i = 3
    j = 8

    if i <= 10:
        for _ in range(j):
            change_color()
            for _ in range(i):
                angle = 360 / i
                sam.right(angle)
                sam.forward(100)
            i += 1

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    sam.pencolor(R,G,B)

def change_color_2():
    turtle.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    sam.pencolor(r, g, b)
def draw_a_random_walk():
    sam.pensize(10)
    directions = [0, 90, 180, 270]
    change_color_2()
    sam.forward(50)
    sam.setheading(random.choice(directions))

def make_a_spirograph(angle):
    nr_of_circles = 360 / angle

    for _ in range(int(nr_of_circles)):
        sam.circle(100)
        sam.right(angle)
        change_color_2()

sam = Turtle()
sam.shape("turtle")
sam.speed("fastest")
sam.color("green")

# challenge 1
# draw_a_square()

# challenge 2
# draw_a_dashed_line()

# challenge 3
# draw_shapes()

# challenge 4
# for _ in range(100):
#     draw_a_random_walk()

# challenge 5
make_a_spirograph(7)

screen = Screen()
screen.exitonclick()