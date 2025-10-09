import turtle as t  # Turtle graphics module for drawing and visualization
import random as r  # Random module for direction & color generation

t.colormode(255)  # Switches Turtle to use RGB values (0–255) instead of named colors


directions = ["right", "left", "forward", "backward"]  # (Unused but here for reference)
direction_angles = [0, 90, 180, 270]  # Four cardinal directions (E, N, W, S)

walk = t.Turtle()  # Our wandering turtle — the star of the show


def random_color():
    """
    Generates a random RGB color tuple.

    Returns:
        tuple[int, int, int]: A 3-value tuple representing (R, G, B) in 0–255 range.


    """
    rc = r.randint(0, 255)
    gc = r.randint(0, 255)
    bc = r.randint(0, 255)
    return (rc, gc, bc)


# --------------------------- TURTLE AESTHETICS---------------------------
walk.shape("arrow")  # So we can see which way it's heading
walk.speed(11)  # 1 = slow, 10 = fastest preset, 11 = "instant zoom"
walk.shapesize(1)  # Default size
walk.width(17)  # Thick pen for bold strokes (so the random walk is clearly visible)

# --------------------------- RANDOM WALK LOOP---------------------------
for i in range(200):
    direction = r.choice(direction_angles)  # Pick a random cardinal direction
    walk.pencolor(random_color())  # Change to a new random RGB color
    walk.forward(30)  # Move ahead
    walk.setheading(direction)  # Instantly rotate to the new direction

# --------------------------- SCREEN EXIT---------------------------
# Keeps the window open until the user clicks, so you can admire the chaos.
screen = t.Screen()
screen.exitonclick()
