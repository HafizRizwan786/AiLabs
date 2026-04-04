import math
"""
# Question 1
cel=float(input('Enter temperature in celsius: '))
fah=(9/5)*cel+32
print(f'{cel} Celsius is {fah:.1f} Fahrenhiet')


# Question 2
radius, length = map(float, input("Enter the radius and length of a cylinder: ").split(","))
area=radius * radius * math.pi
volume=area * length
print(f'The area is {area:.2f}')
print(f'The volume is {volume:.2f}')


# Question 3
employee = {}

employee['name'] = input("Enter employee's name: ")
employee['hours_worked'] = float(input("Enter hours worked: "))
employee['hourly_rate'] = float(input("Enter hourly pay rate: "))
employee['federal_tax_rate'] = float(input("Enter federal tax rate: "))
employee['state_tax_rate'] = float(input("Enter state tax rate: "))


employee['gross_pay'] = employee['hours_worked'] * employee['hourly_rate']
employee['federal_withholding'] = employee['gross_pay'] * employee['federal_tax_rate']
employee['state_withholding'] = employee['gross_pay'] * employee['state_tax_rate']
employee['total_deductions'] = employee['federal_withholding'] + employee['state_withholding']
employee['net_pay'] = employee['gross_pay'] - employee['total_deductions']

print("\nEmployee Name:", employee['name'])
print(f"Gross Pay: ${employee['gross_pay']:.2f}")
print(f"Federal Withholding ({employee['federal_tax_rate']*100:.1f}%): ${employee['federal_withholding']:.1f}")
print(f"State Withholding ({employee['state_tax_rate']*100:.1f}%): ${employee['state_withholding']:.1f}")
print(f"Net Pay: ${employee['net_pay']:.2f}")




# Question 4
amount=int(input('Enter investment amount: '))
annual_interest_rate=float(input('Enter annual interest rate: '))
year=int(input('Enter number of years: '))

monthly_rate=annual_interest_rate/1200
futureValue=amount * (1+monthly_rate) ** (year*12)

print(f'Accumulated value is {futureValue:.2f}')



# Question 5
import turtle

x = float(input("Enter point x: "))
y = float(input("Enter point y: "))

radius = 10
width = 10
height = 5

scale = 20

screen = turtle.Screen()

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)

pen.penup()
pen.goto(0, -radius * scale)
pen.pendown()
pen.pencolor("red")
pen.circle(radius * scale)

left = -(width / 2) * scale
right = (width / 2) * scale
top = (height / 2) * scale
bottom = -(height / 2) * scale

pen.penup()
pen.goto(left, top)
pen.pendown()
pen.pencolor("blue")
pen.goto(right, top)
pen.goto(right, bottom)
pen.goto(left, bottom)
pen.goto(left, top)

if x*2 + y*2 < radius*2:
	circle_result = f"Point ({x:g}, {y:g}) is inside the circle."
else:
	circle_result = f"Point ({x:g}, {y:g}) is outside the circle."

if abs(x) <= width / 2 and abs(y) <= height / 2:
	rectangle_result = f"Point ({x:g}, {y:g}) is inside the rectangle."
else:
	rectangle_result = f"Point ({x:g}, {y:g}) is outside the rectangle."

pen.penup()
pen.goto(x * scale, y * scale)
pen.dot(10, "black")
pen.goto(x * scale + 8, y * scale + 8)
pen.pencolor("black")
pen.write(f"({x:g}, {y:g})")

pen.goto(x * scale + 8, y * scale - 12)
pen.write(circle_result)
pen.goto(x * scale + 8, y * scale - 30)
pen.write(rectangle_result)

turtle.done()



# Question 6
class Book:
    def __init__(self,ISBN,Title,Price,Main_Area,Sub_Area,Pages):
        self.ISBN = ISBN
        self.Title = Title
        self.Price = Price
        self.Main_Area = Main_Area
        self.Sub_Area = Sub_Area
        self.Pages = Pages


    def display(self):
        print(f"ISBN: {self.ISBN}")
        print(f"Title: {self.Title}")
        print(f"Price: ${self.Price:.2f}")
        print(f"Main Area: {self.Main_Area}")
        print(f"Sub Area: {self.Sub_Area}")
        print(f"Pages: {self.Pages}")


book1 = Book("778", "Python ", 29.99, "Computer Science", "Programming", 240)
book1.display()
book2 = Book("928", "Java", 39.99, "Computer Science", "Programming", 572)
book2.display()


# Question 7
class Loan:
    def __init__(self, annualInterestRate=2.5, numberOfYear=1, loanAmount=1000, borrower=" "):
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYear = numberOfYear
        self.__loanAmount = loanAmount
        self.__borrower = borrower
        
    # Getters
    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getNumberOfYear(self):
        return self.__numberOfYear

    def getLoanAmount(self):
        return self.__loanAmount

    def getBorrower(self):
        return self.__borrower

    # Setters
    def setAnnualInterestRate(self, rate):
        self.__annualInterestRate = rate

    def setNumberOfYear(self, year):
        self.__numberOfYear = year

    def setLoanAmount(self, amount):
        self.__loanAmount = amount

    def setBorrower(self, borrower):
        self.__borrower = borrower

    # Calculations
    def getMonthlyPayment(self):
        monthlyInterestRate = self.__annualInterestRate / 1200
        months = self.__numberOfYear * 12
        monthlyPayment = self.__loanAmount * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** -months)
        return monthlyPayment

    def getTotalPayment(self):
        totalPayment = self.getMonthlyPayment() * self.__numberOfYear * 12
        return totalPayment


loan = Loan()
loan.setAnnualInterestRate(5)
loan.setNumberOfYear(1)
loan.setLoanAmount(10000)

print(f"Monthly Payment: Rs {round(loan.getMonthlyPayment(), 2)}")
print(f"Total Payment: Rs {round(loan.getTotalPayment(), 2)}")



# Question 8
class BMI:
    def __init__(self,name,age,weight,height):
        self.__name=name
        self.__age=age
        self.__weight=weight
        self.__height=height
        
    # Getters
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    def getWeight(self):
        return self.__weight
    
    def getHeight(self):
        return self.__height
    
    # Get BMI
    def getBMI(self):
        return self.__weight/self.__height**2
    
    # Get Status
    def getStatus(self):
        bmi=self.getBMI()
        if bmi<18.5:
            return 'Underweight'
        elif bmi>=18.5 and bmi<=24.9:
            return 'Normal'
        elif bmi>=25 and bmi<=29.9:
            return 'Overweight'
        else:
            return 'Obese'
        
person = BMI("Ayan", 22, 70, 1.75)

print(f"Name: {person.getName()}  Age: {person.getAge()}")
print(f"BMI: {person.getBMI():.2f}")
print(f"Status: {person.getStatus()}")
"""


# Question 9
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denom
        imag_part = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.real:.1f} + {self.imag:.1f}i"
    

c1 = Complex(4, 3)
c2 = Complex(2, 1)

print(f"c1 = {c1}, c2 = {c2}")
print(f"c1 - c2 = {c1 - c2}")
print(f"c1 * c2 = {c1 * c2}")
print(f"c1 / c2 = {c1 / c2}")