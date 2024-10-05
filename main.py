import random
import turtle
from turtle import Turtle

import colorgram

color_palette = colorgram.extract("image.jpg", 8)

turtle.colormode(255)

tim = Turtle()

tim.penup()
tim.setx(-250)
tim.sety(-200)
tim.pendown()



tim.speed("fastest")
colors = []

def get_color(index):

    r = color_palette[index].rgb.r
    g = color_palette[index].rgb.g
    b = color_palette[index].rgb.b

    color = (r, g, b)

    return color

for i in range(8):
    colors.append(get_color(i))

for _ in range(10):
    for _ in range(10):
        tim.dot(20,random.choice(colors))
        tim.penup()
        tim.forward(50)
        tim.pendown()

    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)

screen = turtle.Screen()
screen.exitonclick()
