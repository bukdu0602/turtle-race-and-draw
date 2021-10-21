import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "orange", "green", "pink"]cd us
y = -100
is_race_on = False
turtles = []

for i in range(5):
    tim = Turtle(shape="turtle")
    tim.up()
    tim.color(colors[i])
    tim.goto(-230, y)
    y += 40
    turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() == 230:
            is_race_on = False
            if user_bet == turtle.fillcolor():
                print("you won")
            else:
                print("You lose")


# asdfasdfsdfasdfuyihjkjkl345asdfsdfafdsfeasdsadfsdfasdf


screen.exitonclick()