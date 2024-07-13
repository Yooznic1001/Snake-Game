from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.tracer(0)

food = Food()
snake = Snake()
snake.snake()
score = Score()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game = True
while game:
    screen.update()
    snake.move()
    time.sleep(0.1)

    if snake.snakes[0].xcor() > 280 or snake.snakes[0].xcor() < -280 or snake.snakes[0].ycor() > 280 or snake.snakes[0].ycor() < -280:
        game = False
        score.end()



    if snake.snakes[0].distance(food) < 10:
        food.refresh()
        snake.add_snake()
        score.clear()
        score.update()




    for snak in snake.snakes[1:]:

        if snake.snakes[0].distance(snak) < 10:
            game = False
            score.end()



screen.exitonclick()