from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.game_score = 0
        self.high_score=0
        self.write(f"Score: {self.game_score}",move=False,align=ALIGNMENT,font=FONT)
        self.hideturtle()


    def update_score(self):
        self.clear()
        self.game_score += 1
        self.write(f"Score: {self.game_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.game_score > self.high_score:
            self.high_score = self.game_score
        self.game_score = 0
        self.update_score()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align=ALIGNMENT, font=FONT)


