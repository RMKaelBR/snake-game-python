from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Broadway", 20, "normal")


class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.up()
        self.goto(0, 270)
        self.score = 0

    def show(self):
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def increase(self):
        self.score += 1

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)
