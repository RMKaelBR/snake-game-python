from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
STARTING_LENGTH = 3


class Snakey:
    def __init__(self):
        self.snake_parts = []
        self.starting_snake()
        self.head = self.snake_parts[0]

    def x_position(self):
        return self.head.xcor()

    def y_position(self):
        return self.head.ycor()

    def starting_snake(self):
        for first_snake_segments in range(STARTING_LENGTH):
            self.segment_maker()

        for segment in range(len(self.snake_parts)):  # snake_parts[segment].stamp()
            if segment > 0:
                next_spot = (self.snake_parts[segment - 1].xcor() - 20, self.snake_parts[segment].ycor())
                self.snake_parts[segment].goto(next_spot)

    def segment_maker(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.speed("fastest")
        new_segment.pensize(20)
        new_segment.up()
        self.snake_parts.append(new_segment)
        new_segment.goto(self.snake_parts[0].xcor(), self.snake_parts[0].ycor())

    def mover(self):
        if self.wall_collision_checker():
            print("Collision reported!")
            return True

        for part in range(len(self.snake_parts) - 1, 0, -1):
            previous_position = (self.snake_parts[part - 1].xcor(), self.snake_parts[part - 1].ycor())
            self.snake_parts[part].goto(previous_position)

        self.head.forward(MOVE_DISTANCE)

        if self.snake_collision_checker():
            print("Collision reported!")
            return True

        # for part in range(len(snake_parts)):
        #     snake_parts[part].forward(20)
        #     snake_parts[part].stamp()
        # for part in range(len(snake_parts)):
        #     snake_parts[part].clearstamps(1)

        # for part in range(1, len(snake_parts)):
        #     if snake_parts[part].heading() is not snake_parts[part - 1].heading():
        #         snake_parts[part].setheading(snake_parts[part - 1].heading())
        #         break
        # for segment in snake_parts:
        #     segment.forward(20)
        #     segment.stamp()
        # for segment in snake_parts:
        #     segment.clearstamps(1)

    def snake_collision_checker(self):
        if self.head.heading() == RIGHT:
            head_prediction = (round(self.x_position() + 20), round(self.y_position()))
        elif self.head.heading() == UP:
            head_prediction = (round(self.x_position()), round(self.y_position() + 20))
        elif self.head.heading() == LEFT:
            head_prediction = (round(self.x_position() - 20), round(self.y_position()))
        else:  # self.head.heading() == DOWN:
            head_prediction = (round(self.x_position()), round(self.y_position() - 20))

        for part in self.snake_parts[1:]:
            if part.distance(head_prediction) <= 10:
                self.snake_parts[0].color("red")
                part.color("orange")
                print("Collision with snake body.")
                print(f"Head going to: {head_prediction} | segment at: {round(part.xcor()), round(part.ycor())}")
                return True

        # segment_position = (int(segment_x), int(segment_y))
        # head_prediction = (int(self.x_position() + 20), int(self.y_position() + 20))
        #
        # print(f"head: {head_prediction} | segment: {segment_position}")
        # if head_prediction == segment_position:
        #     self.snake_parts[0].color("red")
        #     print("Collision with snake body.")
        #     return True

    def wall_collision_checker(self):
        if self.head.heading() == RIGHT and self.head.xcor() >= 280:
            self.snake_parts[0].color("red")
            print("Collision on East wall.")
            return True
        elif self.head.heading() == UP and self.head.ycor() >= 280:
            self.head.color("red")
            print("Collision on North wall.")
            return True
        elif self.head.heading() == LEFT and self.head.xcor() <= -280:
            self.head.color("red")
            print("Collision on West wall.")
            return True
        elif self.head.heading() == DOWN and self.head.ycor() <= -280:
            self.head.color("red")
            print("Collision on South wall.")
            return True

    def goes_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            print("Turning RIGHT")

    def goes_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            print("Turning UP")

    def goes_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            print("Turning LEFT")

    def goes_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            print("Turning DOWN")
