import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Python Compass Clock")

compass = turtle.Turtle()
compass.color("white")
compass.pensize(3)

for i in range(12):
    compass.penup()
    compass.forward(100)
    compass.pendown()
    compass.forward(20)
    compass.penup()
    compass.forward(20)
    compass.stamp()
    compass.backward(140)
    compass.right(30)

clock = turtle.Turtle()
clock.color("green")
clock.pensize(3)

for i in range(60):
    clock.penup()
    clock.forward(90)
    clock.pendown()
    clock.forward(20)
    clock.penup()
    clock.forward(20)
    clock.stamp()
    clock.backward(130)
    clock.right(6)

while True:
    clock.right(6)
    time.sleep(1)

wn.mainloop()