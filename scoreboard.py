from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 16, 'normal'))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=('Arial', 16, 'normal'))

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 16, 'normal'))
