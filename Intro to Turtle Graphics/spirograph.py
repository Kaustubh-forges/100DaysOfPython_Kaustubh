import turtle as t
import random as r

# Enable RGB color mode for Turtle (values between 0–255)
t.colormode(255)

# Create the drawing turtle
shape = t.Turtle()
shape.speed(3)  # Set moderate drawing speed for better visualization

def random_color():
    """Generate and return a random (R, G, B) color tuple."""
    rc = r.randint(0, 255)
    gc = r.randint(0, 255)
    bc = r.randint(0, 255)
    return (rc, gc, bc)

# Draw the first circle as a base
shape.circle(100)
# Tilt the turtle to change orientation slightly
shape.tilt(30)
# Move forward to offset the next circle's position
shape.forward(20)
# Draw another circle in the new position
shape.circle(100)

# Track the turtle's heading angle for rotations
s = shape.heading()

# Draw multiple circles rotated by 20° each to form the spirograph
for i in range(360 // 20):  # 360/20 = 18 iterations for a full rotation
    shape.circle(100)
    color = random_color()
    shape.pencolor(color)      # Change pen color for each circle
    shape.setheading(s + 20)   # Increment heading by 20° for the next circle
    s += 20                    # Update the heading tracker

# Keep the window open until user clicks
screen = t.Screen()
screen.exitonclick()
