from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create()
        self.head = self.body[0]

    def create(self):
        for body_part_index in range(0, 3):
            snake_part = Turtle("square")
            snake_part.color("white")
            snake_part.penup()
            self.body.append(snake_part)
            self.body[body_part_index].goto(self.body[body_part_index - 1].xcor() - 20,
                                            self.body[body_part_index - 1].ycor())

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
