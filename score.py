from turtle import Turtle
POSITION_LEFT = (-100,200)
POSITION_RIGHT = (100,200)
ALIGNMENT = "center"
FONT = ("Courier", "60", "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0

    def update_score_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score , align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score +=1
        self.update_score_board()

    def r_point(self):
        self.r_score +=1
        self.update_score_board()