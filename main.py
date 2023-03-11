"""---------------------------------------- Bet on The Turtles ----------------------------------------
In this code, a simple betting game.
"""

# ---------------------------------------- Add Required Library ----------------------------------------

from random import randint
from turtle import Turtle, Screen

# ---------------------------------------- Get Guesses from User ----------------------------------------

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet",
                            prompt="Whiche turtle will win the race?\n(Choose one of the colors red, orange, yellow, green, blue, purple.)\nYou can also not guess and just enjoy watching the match.")
print("User Bet: ", user_bet)

# ---------------------------------------- Turtles Defenition ----------------------------------------

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -48, -10, 20, 50, 88]

# ---------------------------------------- Turtles on the race Placementation ----------------------------------------

all_turtle = []
for i in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-100, y=y_position[i])
    all_turtle.append(tim)

# ---------------------------------------- Race Running ----------------------------------------

while not user_bet == "":
    for t in all_turtle:
        if t.xcor() > 200:
            user_bet = ""
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print("you've won!")
            else:
                print(f"you've lost. The {winning_color} turtle is the winner!")
        rand_dis = randint(0, 10)
        t.forward(rand_dis)

screen.exitonclick()
