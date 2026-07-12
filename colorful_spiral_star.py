#Colorful Spiral Star
import turtle
star = turtle.Turtle()
star.speed(10)
star.pensize(2)
star.hideturtle()
screen = turtle.Screen()
screen.bgcolor("black")

colors = ['cyan', 'blue', 'purple', 'magenta', 'white']

for i in range(70):
    star.color(colors[i % len(colors)])
    
    star.forward(i * 10)
    star.right(144)
    
turtle.done()