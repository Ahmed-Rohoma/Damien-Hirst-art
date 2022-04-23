import turtle
from turtle import Turtle, Screen
from random import choice

turtle.colormode(255)


class Hirst:
    def __init__(self, color):
        self.tim = Turtle()
        self.tim.hideturtle()
        self.tim.speed("fast")
        self.y = -280
        self.color = color
        self.draw(self.color)

    def draw(self, color):
        for j in range(10):
            self.y += 50
            self.tim.penup()
            self.tim.setpos(-220, self.y)
            for i in range(10):
                self.tim.dot(20,choice(color))
                self.tim.forward(50)
        screen = Screen()
        screen.exitonclick()

    def draw_without_nested_loop(self, color):
        self.tim.penup()
        for i in range(100):
            if i % 10 == 0:
                self.y += 50
                self.tim.setpos(-220, self.y)
            self.tim.dot(20, choice(color))
            self.tim.forward(50)



