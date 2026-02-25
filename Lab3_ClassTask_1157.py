# Task 1
# import turtle 
# t1=turtle.Turtle()
# t1.shape('circle')
# t1.color('green')
# turtle.bgcolor('grey')
# turtle.title('This the shape of the circle')
# t1.forward(100)
# t1.right(90)
# t1.backward(50)
# t1.circle(25)

# turtle.done()


# Task 2
# import turtle

# turtle.showturtle()
# turtle.backward(50)
# turtle.right(70)
# turtle.forward(50)
# turtle.goto(50,50)
# turtle.penup()
# turtle.pendown()
# turtle.circle(45)
# turtle.color('blue')
# turtle.pensize(3)

# turtle.done()


# Task 3
# import turtle

# turtle.pensize(3)
# turtle.color('red')

# # Triangle
# turtle.penup()
# turtle.goto(-200,-50)
# turtle.pendown()
# turtle.circle(40,steps=3)

# # Rectangle
# turtle.penup()
# turtle.goto(-100,-50)
# turtle.pendown()
# turtle.circle(40,steps=4)

# # Pentagon
# turtle.penup()
# turtle.goto(0,-50)
# turtle.pendown()
# turtle.circle(40,steps=5)


# turtle.done()


# Task 3
# import turtle
# x1=int(input('Enter x1: '))
# y1=int(input('Enter y1: '))
# x2=int(input('Enter x2: '))
# y2=int(input('Enter y2: '))
# distance=((x2-x1)**2 + (y2-y1)**2) **0.5

# turtle.penup()
# turtle.goto(x1,y1)
# turtle.write('P1')
# turtle.pendown()
# turtle.goto(x2,y2)
# turtle.write('P2')
# turtle.penup()
# turtle.goto((x1+x2)/2,(y1+y2)/2)
# turtle.write(distance)
# turtle.hideturtle()
# turtle.done()



# Task 4
# import turtle
# x1=int(input('Enter x1: '))
# y1=int(input('Enter y1: '))
# x2=int(input('Enter x2: '))
# y2=int(input('Enter y2: '))
# x3=int(input('Enter radius: '))
# d=((x2-x1)**2 + (y2-y1)**2) **0.5

# turtle.pensize(3)
# turtle.pencolor('red')
# turtle.penup()
# turtle.goto(x1,y1)
# turtle.pendown()
# turtle.circle(x3)
# turtle.penup()
# turtle.goto(x2,y2)
# turtle.begin_fill()
# turtle.color('purple')
# turtle.pendown()
# turtle.circle(2)
# turtle.goto(x2,y2+3)
# turtle.write('P1')
# turtle.end_fill()
# turtle.penup()
# turtle.goto(x1-x3,y1-x3)
# if d<=x3:
#     turtle.write('Point P1 is inside',font=('Times',18,'bold'))
# else:
#     turtle.write("Point P1 is outside",font=('Times',18,'bold'))
# turtle.hideturtle()
# turtle.done()



# Task 5
# import turtle
# turtle.shape('turtle')

# turtle.pensize(3)
# turtle.color('blue')
# turtle.penup()
# turtle.goto(-150,10)
# turtle.pendown()
# turtle.circle(50)

# turtle.color('yellow')
# turtle.penup()
# turtle.goto(-96,-50)
# turtle.pendown()
# turtle.circle(50)

# turtle.color('black')
# turtle.penup()
# turtle.goto(-40,10)
# turtle.pendown()
# turtle.circle(50)

# turtle.color('green')
# turtle.penup()
# turtle.goto(14,-50)
# turtle.pendown()
# turtle.circle(50)

# turtle.color('red')
# turtle.penup()
# turtle.goto(70,10)
# turtle.pendown()
# turtle.circle(50)

# turtle.done()



# Task 6
# class Dog:
#     atr1='mamal'
#     atr2='dog'
    
#     def fun(self):
#         print('I am a ',self.atr1)
#         print('I am a ',self.atr2)
        
# Rodger=Dog()
# print(Rodger.atr1)
# Rodger.fun()



# Task 7
import turtle
class circle:
    x=10
    y=10
    radius=50
    def drawCircle(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.circle(self.radius)
        
a=circle()
a.drawCircle()