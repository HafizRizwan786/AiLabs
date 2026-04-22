import turtle
import math

# Input from user
x = int(input("Enter x-coordinate of center: "))
y = int(input("Enter y-coordinate of center: "))
r = int(input("Enter radius of circle: "))

# Move to starting point (bottom of circle)
turtle.penup()
turtle.goto(x, y - r)
turtle.pendown()

# Draw circle
turtle.circle(r)

# Calculate area
area = math.pi * r * r

# Write area at center
turtle.penup()
turtle.goto(x, y)
turtle.write(f"Area = {area:.2f}", align="center", font=("Arial", 12, "bold"))

# Hide turtle and finish
turtle.hideturtle()
turtle.done()