from turtle import Turtle
import random
COORDINATES = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100,
               120, 140, 160, 180, 200, 220, 240, 260, 280]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color("green")
        self.speed("fastest")
        self.shapesize(0.5, 0.5)
        self.maker()

    def maker(self):
        self.goto(random.choice(COORDINATES), random.choice(COORDINATES))

    def eat(self, snake):
        if self.distance(snake.head) < 19:
            self.maker()
            return True
        else:
            return 0

        # food_position = (self.xcor(), self.ycor())
        # snake_head_position = (snake.x_position(), snake.y_position())
        # print(f"{food_position} {snake_head_position}")
        # if food_position == snake_head_position:
        #     print(f"Current score: {score + 1}")
        #     return self.maker()

