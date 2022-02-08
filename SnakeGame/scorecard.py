from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",12,"normal")

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)


    
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Arial",12,"normal"))

