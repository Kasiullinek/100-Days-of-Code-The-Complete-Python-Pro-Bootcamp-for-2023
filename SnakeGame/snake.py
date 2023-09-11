from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.body = []
        self.create()
        self.head = self.body[0]

    def create(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.body.append(snake_part)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for body_part_index in range(len(self.body) - 1, 0, -1):
            new_x = self.body[body_part_index - 1].xcor()
            new_y = self.body[body_part_index - 1].ycor()
            self.body[body_part_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_north(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_south(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_east(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_west(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
