from turtle import Turtle






STARTING_POSITION=(0,-280)
MOVED=10
FINISH=280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        # self.color('black')
        self.start()
        self.setheading(90)

    def tup(self):
        self.forward(MOVED)
    
    def start(self):
        self.goto(STARTING_POSITION)
    def finish(self):
        if self.ycor()>280:
            return True
        else:
            return False

    