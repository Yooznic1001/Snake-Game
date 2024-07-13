from turtle import Turtle

class Snake:

    def __init__(self):
        self.snakes = []

    def snake(self):
        x = 0
        for _ in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(x=x, y=0)
            x -= 20
            self.snakes.append(snake)

    def add_snake(self):
        xpos = self.snakes[-1].xcor()
        ypos = self.snakes[-1].ycor()
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(x=xpos, y=ypos)
        self.snakes.append(snake)



    def move(self):
        for seg in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg - 1].xcor()
            new_y = self.snakes[seg - 1].ycor()
            self.snakes[seg].goto(new_x, new_y)
        self.snakes[0].forward(20)

    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

