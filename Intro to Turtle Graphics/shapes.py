# ------------------- Module Imports -------------------
import turtle as t  # 'turtle' module is used for creating graphics and drawings
import random as r  # 'random' module used for choosing random colors for each shape

# ------------------- Turtle (Player) Setup -------------------
Player = t.Turtle()  # Creating a turtle object named 'Player'
Player.shape("arrow")  # Setting the shape of the turtle cursor to an arrow

# ------------------- Constants and Data -------------------
CONSTANT = 360  # Represents the total degrees in a circle; used for angle calculation
colors = ["Red", "Blue", "Green", "Yellow"]  # Color palette for random shape coloring

# ------------------- Function Definition -------------------
def generate_shape(lines: int):
    Player.color(r.choice(colors))  # Assign a random color for the current shape
    for line in range(lines):
        Player.forward(100)  # Draw one side
        Player.right(CONSTANT / lines)  # Turn based on the shape's required angle


# ------------------- Shape Generation Loop -------------------
# Draws polygons with number of sides ranging from 3 (triangle) to 10 (decagon)
for lines in range(3, 11):
    generate_shape(lines)

# ------------------- Screen Exit -------------------
# Keeps the window open until user clicks inside it
screen = t.Screen()
screen.exitonclick()
