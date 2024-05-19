from turtle import Screen
import time
from player import Player
from car import Car
from score import Score



myscr=Screen()
myscr.setup(height=600,width=600)
myscr.tracer(0)
myscr.title('TURTLE CROSS 🐢')

players=Player()
cars=Car()
score=Score()

myscr.listen()
myscr.onkey(players.tup,'Up')
game=True
while game:
    time.sleep(0.1)
    myscr.update()
    cars.ccar()
    cars.movecar()

    #Turtle Car collision
    for car in cars.allcar:
        if car.distance(players)<20:
            # print("COOO")
            score.gamovr()
            game=False
    

    #Other side
    if players.finish():
        players.start()
        cars.levelup()
        score.inc()
    

    
    






















































































myscr.exitonclick()