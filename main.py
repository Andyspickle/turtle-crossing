from turtle import Screen
from player import Player
from carmanager import CarManager
import time
import random
WIDTH, HEIGHT = 600, 600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)
screen.colormode(255)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.go_up, "Up")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() == 290:
        is_game_on = False
        print("You win!")


screen.exitonclick()
