#====Question 3=========
import turtle
import math
t=turtle.Turtle()
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
r1 = int(input("Enter radius1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
r2 = int(input("Enter radius2: "))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

t.speed(0)

t.penup()
t.goto(x1, y1-r1)
t.pendown()
t.color("red")
t.circle(r1)

t.penup()
t.goto(x2, y2-r2)
t.pendown()
t.color("blue")
t.circle(r2)


t.penup()
t.goto(-200, 200)

if distance + r2 <= r1:
    t.write("Circle2 is inside Circle1", font=("Arial",16,"bold"))

elif distance <= r1 + r2:
    t.write("Circle2 overlaps Circle1", font=("Arial",16,"bold"))

else:
    t.write("No Overlap", font=("Arial",16,"bold"))

t.hideturtle()
t.done()