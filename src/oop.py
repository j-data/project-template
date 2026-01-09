from turtle import *


def star(t, color, width, fsize, lsize):
    t.color(color)
    t.width(width)
    t.begin_fill()
    for i in range(5):
        t.forward(fsize)
        t.left(lsize)
    t.end_fill()


def circle(t, color, width, radius):
    t.color(color)
    t.width(width)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


t = Turtle()

# Ask for user's input
ask = input("Enter a shape from either 'star' or 'circle' or enter 'exit' to quit: ").strip().lower()
while ask != "exit":
    if ask == "star":
        color = input("Enter a color for the star: ").strip().lower()
        width = int(input("Enter a width for the star: ").strip().lower())
        fsize = int(input("Enter a forward size for the star: ").strip().lower())
        lsize = int(input("Enter a left size for the star: ").strip().lower())
        star(t, color, width, fsize, lsize)
    elif ask == "circle":
        color = input("Enter a color for the circle: ").strip().lower()
        width = int(input("Enter a width for the circle: ").strip().lower())
        radius = int(input("Enter a radius for the circle: ").strip().lower())
        circle(t, color, width, radius)
    else:
        print("Invalid shape. Please enter 'star' or 'circle'.")
    ask = input("Enter a shape from either 'star' or 'circle' or enter 'exit' to quit: ").strip().lower()
done()
