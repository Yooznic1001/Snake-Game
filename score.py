from food import Food
from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-50, 270)
        self.write(f"score : {self.score}", font=("Arial", 20, "normal"))

    def update(self):
        self.score += 1
        self.write(f"score : {self.score}", font=("Arial", 20, "normal"))

    def end(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER",align="center", font=("Arial", 36, "normal"))
        self.goto(0, -50)
        self.write(f"Your score {self.score}", align="center", font=("Arial", 36, "normal"))