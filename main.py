from turtle import Screen, Turtle
from snakeysnake import Snakey
from food import Food
from scoreboard import Score_board
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake in Python")
screen.tracer(0)
screen.listen()
snake = Snakey()
food = Food()
scoreboard = Score_board()

screen.onkeypress(snake.goes_right, "Right")
screen.onkeypress(snake.goes_up, "Up")
screen.onkeypress(snake.goes_left, "Left")
screen.onkeypress(snake.goes_down, "Down")
game_is_on = True

food.maker()

while game_is_on:
    screen.update()
    time.sleep(.1)
    scoreboard.show()

    if snake.mover():
        screen.update()
        scoreboard.game_over()
        print("Ending.")
        game_is_on = False

    if food.eat(snake):
        scoreboard.increase()
        snake.segment_maker()






screen.exitonclick()
