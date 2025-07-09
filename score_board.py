from turtle import Turtle

class ScoreBoard():

    def __init__(self, position):
        super().__init__()
        self.current_score = 0
        self.score = Turtle()
        self.score.penup()
        self.score.color("white")
        self.score.goto(position)
        self.update_score()
        self.score.hideturtle()

    def update_score(self):
        self.score.write(arg=f"{self.current_score}", align="center", font=("Courier", 60, "bold"))

    def clear_score(self):
        self.score.clear()

    def increase_score(self):
        self.current_score += 1
        self.update_score()
