# ------------------------ Modules Imported ------------------
import turtle as t
import random

# Set the color mode to RGB for more flexibility in color usage
t.colormode(255)
t.hideturtle()


# Pre-extracted color palette from Hirst painting using colorgram
colors = [
    (99, 51, 6), (172, 33, 158), (75, 172, 94), (232, 73, 209),
    (10, 127, 35), (212, 34, 91), (177, 155, 104), (104, 210, 122),
    (25, 40, 95), (33, 48, 103), (112, 212, 130), (183, 161, 115),
    (218, 40, 92)
]

# Marks the start point for first dot
x = -250
y = -200

# Draws a single row of 10 randomly colored dots
def per_row_insertion(colors):
    x = -250
    dots = 0
    global y
    while dots < 10: # Marks number of dots in a row
        new_dot = t.Turtle()
        new_dot.speed(7)
        new_dot.penup()
        new_dot.shape("circle")
        new_dot.color(random.choice(colors))
        new_dot.goto((x, y))
        x += 50 # Moves by 50 units for the next dot in the row
        dots += 1

# Draw 10 rows to form a 10x10 dot grid
rows = 0
while rows < 10:
    per_row_insertion(colors)
    y += 50
    rows += 1

screen = t.Screen()
screen.exitonclick()
