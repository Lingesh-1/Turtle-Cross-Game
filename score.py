from turtle import Turtle

FONT=('corier',16,'normal')



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.levl=1
        self.hideturtle()
        self.penup()
        self.goto(x=-280,y=260)
        self.upd()
        # self.write(f"Level:{self.levl}",font=FONT,align='left')
    def upd(self):
        self.clear()
        self.write(f"Level:{self.levl}",font=FONT,align='left')
    def inc(self):
        self.levl+=1
        self.upd()

    def gamovr(self):
        self.goto(0,0)
        self.write(f"Game Overr!!!!",align='center',font=FONT)
        