import random
import turtle
import colorgram
from turtle import Turtle, Screen

def extract_colors(nr_of_colors):
    """This function extracts the given number of colors from image.jpg"""

    extracted_colors = colorgram.extract("image.jpg", nr_of_colors)
    turtle.colormode(255)
    colors = []
    i = 0
    for i in range(len(extracted_colors)):
        r = extracted_colors[i].rgb.r
        g = extracted_colors[i].rgb.g
        b = extracted_colors[i].rgb.b
        color = (r, g, b)
        colors.append(color)
        print(colors[i])
        i += 1

    return colors

def draw_image():
    nr_of_circles = 5
    radius = 10
    space = 25
    colors = extract_colors(10)

    for _ in range(nr_of_circles):
        for _ in range(nr_of_circles):
            sam.color(random.choice(colors))
            sam.begin_fill()
            sam.circle(radius)
            sam.end_fill()
            sam.penup()
            sam.forward(radius*2)
            sam.forward(space)
            sam.pendown()
        sam.penup()
        sam.back(nr_of_circles*radius*2 + nr_of_circles*space)
        sam.setheading(90)
        sam.forward(radius*2 + space)
        sam.setheading(0)
    sam.hideturtle()

sam = Turtle()
sam.speed("fastest")

draw_image()

screen = Screen()
screen.exitonclick()