# Quetion 1
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



# Question 2
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




# Question 3
class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    def __sub__(self, other):
        return Complex(self.__real - other.__real,self.__img - other.__img)

    def __mul__(self, other):
        return Complex(self.__real*other.__real - self.__img*other.__img,
                       self.__real*other.__img + self.__img*other.__real)

    def __truediv__(self, other):
        denom = other.__real**2 + other.__img**2
        return Complex((self.__real*other.__real + self.__img*other.__img)/denom,
                       (self.__img*other.__real - self.__real*other.__img)/denom)

    def __str__(self):
        return f"{self.__real} + {self.__img}i"


c1 = Complex(2, 3)
c2 = Complex(3, 4)

print(c1 * c2)
print(c1 - c2)
print(c1 / c2)




# Question 4
import math
class RationalNumber:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Denominator cannot be zero")

        # Avoid negative denominator
        if den < 0:
            num = -num
            den = -den

        # Reduce fraction
        g = math.gcd(abs(num), abs(den))
        self.num = num // g
        self.den = den // g
        

    def __add__(self, other):
        return RationalNumber(
            self.num * other.den + other.num * self.den,
            self.den * other.den
        )

    def __sub__(self, other):
        return RationalNumber(
            self.num * other.den - other.num * self.den,
            self.den * other.den
        )

    def __mul__(self, other):
        return RationalNumber(
            self.num * other.num,
            self.den * other.den
        )

    def __truediv__(self, other):
        if other.num == 0:
            raise ValueError("Cannot divide by zero")
        return RationalNumber(
            self.num * other.den,
            self.den * other.num
        )


    # -------- Relational & Equality Operators --------
    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den

    def __le__(self, other):
        return self.num * other.den <= other.num * self.den

    def __gt__(self, other):
        return self.num * other.den > other.num * self.den

    def __ge__(self, other):
        return self.num * other.den >= other.num * self.den

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return f"{self.num}/{self.den}"


r1 = RationalNumber(4, 8)
r2 = RationalNumber(3, 6)

print(r1)
print(r2)

print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
print(r1 / r2)

print(r1 == r2)
print(r1 < r2)
print(r1 >= r2)



# Question 5
class Polynomial:
    # Constructor
    def __init__(self, terms=None):
        if terms is None:
            self.terms = []
        else:
            self.terms = terms
        self._simplify()

    # Destructor
    def __del__(self):
        print("Polynomial object destroyed")

    def get_terms(self):
        return self.terms

    def set_terms(self, terms):
        self.terms = terms
        self._simplify()


    # Private method to simplify polynomial
    def _simplify(self):
        result = {}
        for coeff, exp in self.terms:
            if exp in result:
                result[exp] += coeff
            else:
                result[exp] = coeff

        # Remove zero coefficients
        self.terms = [(c, e) for e, c in result.items() if c != 0]

        # Sort in descending order of exponent
        self.terms.sort(key=lambda x: x[1], reverse=True)


    # Addition +
    def __add__(self, other):
        new_terms = self.terms + other.terms
        return Polynomial(new_terms)

    # Subtraction -
    def __sub__(self, other):
        neg_terms = [(-c, e) for c, e in other.terms]
        new_terms = self.terms + neg_terms
        return Polynomial(new_terms)

    # Multiplication *
    def __mul__(self, other):
        result_terms = []
        for c1, e1 in self.terms:
            for c2, e2 in other.terms:
                result_terms.append((c1 * c2, e1 + e2))
        return Polynomial(result_terms)

    # Assignment =
    def __eq__(self, other):
        return self.terms == other.terms

    # +=
    def __iadd__(self, other):
        self.terms += other.terms
        self._simplify()
        return self

    # -=
    def __isub__(self, other):
        self.terms += [(-c, e) for c, e in other.terms]
        self._simplify()
        return self

    # *=
    def __imul__(self, other):
        result = []
        for c1, e1 in self.terms:
            for c2, e2 in other.terms:
                result.append((c1 * c2, e1 + e2))
        self.terms = result
        self._simplify()
        return self


    def __str__(self):
        if not self.terms:
            return "0"

        result = ""
        for coeff, exp in self.terms:
            if coeff > 0 and result:
                result += " + "
            elif coeff < 0:
                result += " - "
                coeff = abs(coeff)

            if exp == 0:
                result += f"{coeff}"
            elif exp == 1:
                result += f"{coeff}x"
            else:
                result += f"{coeff}x^{exp}"

        return result
    
    
p1 = Polynomial([(2,4), (3,2), (5,0)])
p2 = Polynomial([(1,3), (4,2)])

print("P1 =", p1)
print("P2 =", p2)

print("Addition:", p1 + p2)
print("Subtraction:", p1 - p2)
print("Multiplication:", p1 * p2)

p1 += p2
print("After += :", p1)

