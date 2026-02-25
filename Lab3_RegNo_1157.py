import turtle
import math

# Question 1
"""
width=int(input('Enter width: '))
height=int(input('Enter height: '))
x=int(input('Enter x: '))
y=int(input('Enter y: '))

turtle.pensize(3)
turtle.color('green')
turtle.penup()
turtle.goto(x,y)
turtle.pendown()

for i in range(2):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    
turtle.done()


# Question 2
x1=int(input("Enter the value of x1  : "))
y1=int(input("Enter the value of y1 : "))
x2=int(input("Enter the value of the x2  : "))
y2=int(input("Enter the value of the  y2 : "))
x3=int(input("Enter Radius  : "))
distance=((x1-x2)**2+(y1-y2)**2)**0.5
turtle.pensize(3)
turtle.color("red")
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.circle(x3)
turtle.penup()
turtle.goto(x2,y2)
turtle.begin_fill()
turtle.color("purple")
turtle.pendown()
turtle.circle(2)
turtle.goto(x2,y2+3)
turtle.write("p1")
turtle.end_fill()
turtle.penup()
turtle.goto(x1-x3,y1-x3)
if distance<=x3:
    turtle.write("P1 is inside the circle",font=("Times",18,"bold"))
else:
    turtle.write("P1 is the outside the circle ")
    
turtle.done()


# Question 3
# For Circle
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
r1 = int(input("Enter radius1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
r2 = int(input("Enter radius2: "))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

turtle.speed(0)

turtle.penup()
turtle.goto(x1, y1-r1)
turtle.pendown()
turtle.color("red")
turtle.circle(r1)

turtle.penup()
turtle.goto(x2, y2-r2)
turtle.pendown()
turtle.color("blue")
turtle.circle(r2)


turtle.penup()
turtle.goto(-200, 200)

if distance + r2 <= r1:
    turtle.write("Circle2 is inside Circle1", font=("Arial",16,"bold"))

elif distance <= r1 + r2:
    turtle.write("Circle2 overlaps Circle1", font=("Arial",16,"bold"))

else:
    turtle.write("No Overlap", font=("Arial",16,"bold"))

turtle.done()


# For Rectangle
r1x = int(input("Enter Rectangle1 center x: "))
r1y = int(input("Enter Rectangle1 center y: "))
w1 = int(input("Enter Rectangle1 width: "))
h1 = int(input("Enter Rectangle1 height: "))

r2x = int(input("Enter Rectangle2 center x: "))
r2y = int(input("Enter Rectangle2 center y: "))
w2 = int(input("Enter Rectangle2 width: "))
h2 = int(input("Enter Rectangle2 height: "))

# Draw Rectangle 1
turtle.penup()
turtle.goto(r1x - w1/2, r1y - h1/2)
turtle.pendown()
turtle.color("green")

for i in range(2):
    turtle.forward(w1)
    turtle.left(90)
    turtle.forward(h1)
    turtle.left(90)

# Draw Rectangle 2
turtle.penup()
turtle.goto(r2x - w2/2, r2y - h2/2)
turtle.pendown()
turtle.color("purple")

for i in range(2):
    turtle.forward(w2)
    turtle.left(90)
    turtle.forward(h2)
    turtle.left(90)

# Rectangle boundaries
left1 = r1x - w1/2
right1 = r1x + w1/2
top1 = r1y + h1/2
bottom1 = r1y - h1/2

left2 = r2x - w2/2
right2 = r2x + w2/2
top2 = r2y + h2/2
bottom2 = r2y - h2/2

# Write result for rectangles
turtle.penup()
turtle.goto(-200, -250)
turtle.color("black")

if (left2 >= left1 and right2 <= right1 and
    top2 <= top1 and bottom2 >= bottom1):
    turtle.write("Rectangle 2 is inside Rectangle 1", font=("Arial", 14, "bold"))
elif not (right2 < left1 or left2 > right1 or
          top2 < bottom1 or bottom2 > top1):
    turtle.write("Rectangle 2 overlaps Rectangle 1", font=("Arial", 14, "bold"))
else:
    turtle.write("Rectangle 2 does not overlap Rectangle 1", font=("Arial", 14, "bold"))

turtle.hideturtle()
turtle.done()



# Question 4
class Book:
    def __init__(self, ISBN, title, price, main_area, sub_area, no_of_pages):
        self.ISBN = ISBN
        self.title = title
        self.price = price
        self.main_area = main_area
        self.sub_area = sub_area
        self.no_of_pages = no_of_pages

    def show(self):
        print(f"ISBN: {self.ISBN}")
        print(f"Title: {self.title}")
        print(f"Price: ${self.price}")
        print(f"Main Area: {self.main_area}")
        print(f"Sub Area: {self.sub_area}")
        print(f"No. of Pages: {self.no_of_pages}")


book1 = Book("978-0135166307", "Python Programming", 45.99, "Computer Science", "Programming", 550)
book1.show()


print('\n\n')

# Question 5
class Computer:
    def __init__(self, brand_name, speed, memory_size):
        self.brand_name = brand_name
        self.speed = speed         
        self.memory_size = memory_size 

    def show(self):
        print(f"Brand Name: {self.brand_name}")
        print(f"Speed: {self.speed} GHz")
        print(f"Memory Size: {self.memory_size} GB")


comp1 = Computer("Dell", 3.5, 16)
comp1.show()


print('\n\n')

# Question 6
class Loan:
    def __init__(self, annualInterestRate=2.5, numberOfYears=1, loanAmount=1000, borrower=""):
        self.__annualInterestRate = annualInterestRate  
        self.__numberOfYears = numberOfYears            
        self.__loanAmount = loanAmount                  
        self.__borrower = borrower                      

    # ---------------- Getters ----------------
    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getNumberOfYears(self):
        return self.__numberOfYears

    def getLoanAmount(self):
        return self.__loanAmount

    def getBorrower(self):
        return self.__borrower

    # ---------------- Setters ----------------
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def setNumberOfYears(self, numberOfYears):
        self.__numberOfYears = numberOfYears

    def setLoanAmount(self, loanAmount):
        self.__loanAmount = loanAmount

    def setBorrower(self, borrower):
        self.__borrower = borrower

    # ---------------- Calculations ----------------
    def getMonthlyPayment(self):
        monthlyInterestRate = self.__annualInterestRate / 1200
        months = self.__numberOfYears * 12
        monthlyPayment = self.__loanAmount * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** -months)
        return monthlyPayment

    def getTotalPayment(self):
        totalPayment = self.getMonthlyPayment() * self.__numberOfYears * 12
        return totalPayment


loan1 = Loan(annualInterestRate=3.5, numberOfYears=5, loanAmount=10000, borrower="Hafiz Rizwan")
# Access and display properties
print("Borrower:", loan1.getBorrower())
print("Annual Interest Rate:", loan1.getAnnualInterestRate())
print("Number of Years:", loan1.getNumberOfYears())
print("Loan Amount:", loan1.getLoanAmount())

# Calculate monthly and total payments
print(f"Monthly Payment: ${loan1.getMonthlyPayment():.2f}")
print(f"Total Payment: ${loan1.getTotalPayment():.2f}")

# Update some properties
loan1.setAnnualInterestRate(4.0)
loan1.setLoanAmount(15000)

print("\nAfter updating interest rate and loan amount:")
print(f"Monthly Payment: ${loan1.getMonthlyPayment():.2f}")
print(f"Total Payment: ${loan1.getTotalPayment():.2f}")


"""
# Question 7
class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight   
        self.__height = height 

    # Getter methods
    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getWeight(self):
        return self.__weight

    def getHeight(self):
        return self.__height

    # Calculate BMI
    def getBMI(self):
        bmi = self.__weight / (self.__height ** 2)
        return bmi

    # Determine BMI Status
    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"


person1 = BMI("Hafiz Rizwan", 22, 68, 1.75)
print("Name:", person1.getName())
print("Age:", person1.getAge())
print("Weight:", person1.getWeight(), "kg")
print("Height:", person1.getHeight(), "m")
print("BMI: {:.2f}".format(person1.getBMI()))
print("Status:", person1.getStatus())



