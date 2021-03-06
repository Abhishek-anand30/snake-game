from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",14,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.score=0
        self.update_score()
    def update_score(self):
        self.write(f"Score:{self.score}",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def new_score(self):
        self.score +=1
        self.clear()
        self.update_score()

