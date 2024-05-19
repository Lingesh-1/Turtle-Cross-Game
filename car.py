from turtle import Turtle
import random as r



COLORS=['red','orange','yellow','green','blue','purple']
STARTING=5
MOVEIN=10


class Car:
    def __init__(self):
        self.allcar=[]
        self.startspeed=STARTING
        # super().__init__()
        # self.shape('square')
        # self.penup()
        # self.shapesize()
        # self.goto(STARTING)
    def ccar(self):
        rans=r.randint(1,6)
        if rans==1:
            new=Turtle('square')
            new.shapesize(stretch_len=2,stretch_wid=1)
            new.penup()

            new.color(r.choice(COLORS))
            randy= r.randint(-250,250)
            new.goto(300,randy)
            self.allcar.append(new)

    def movecar(self):
        for i in self.allcar:
            i.backward(self.startspeed)
    
    def levelup(self):
        self.startspeed+=MOVEIN