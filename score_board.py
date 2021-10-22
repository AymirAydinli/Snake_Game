from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.write(arg=f"Score: {self.score}", align='center', font=("Arial", 14, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        return self.write(arg=f"Score: {self.score}", align='center', font=("Arial", 14, "normal"))

    def game_over(self):
        #self.penup()
        self.goto(0, 0)
        self.color("white")
        self.hideturtle()
        return self.write(arg="GAME OVER", align='center', font=("Arial", 30, "bold"))
