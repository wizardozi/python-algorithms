from p5 import *

x, y = 300, 300
x_speed, y_speed = 3, 3

def setup():
    size(600, 600)
    title("Bouncing Circle")

def draw():
    global x, y, x_speed, y_speed

    background(30)  # Dark background
    fill(200, 50, 100)  # Circle color
    ellipse(x, y, 50, 50)

    # Move the circle
    x += x_speed
    y += y_speed

    # Bounce off edges
    if x > width or x < 0:
        x_speed *= -1
    if y > height or y < 0:
        y_speed *= -1

run()
