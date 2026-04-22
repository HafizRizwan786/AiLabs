import math
# Question 1
cel=int(input("Enter Temperature in Celsius: "))
f=(9/5)*cel+32
print(f"{cel} Celsius is {f} Fahrenheit")


# Question 2
r=float(input('Enter radius: '))
l=int(input('Enter length: '))
a=math.pi*r*r
v=a*l
print(f"The area is {a}")
print(f"The volume is {v}")


# Question 3
f=float(input('Enter a value in feets: '))
m=f*0.305
print(f"{f} feet is {m} meters")


# Question 4
p=float(input('Enter a value in pounds: '))
kg = p * 0.454
print(f"{p} pounds is {kg} kilograms")



# Question 5
sub=float(input('Enter the subtotals: '))
rate=float(input('Enter the gratuity rate: '))
gratuity=(sub * rate) / 100
total=sub+gratuity
print(f"Gratuity is {gratuity}")
print(f"The total is {total}")


# Question 6
employee = {}

employee['name'] = input("Enter employee's name: ")
employee['hours_worked'] = float(input("Enter number of hours worked in a week: "))
employee['hourly_rate'] = float(input("Enter hourly pay rate: "))
employee['federal_tax_rate'] = float(input("Enter federal tax withholding rate (as decimal, e.g., 0.2 for 20%): "))
employee['state_tax_rate'] = float(input("Enter state tax withholding rate (as decimal, e.g., 0.09 for 9%): "))

# Calculate gross pay
employee['gross_pay'] = employee['hours_worked'] * employee['hourly_rate']

# Calculate deductions
employee['federal_withholding'] = employee['gross_pay'] * employee['federal_tax_rate']
employee['state_withholding'] = employee['gross_pay'] * employee['state_tax_rate']
employee['total_deductions'] = employee['federal_withholding'] + employee['state_withholding']

# Calculate net pay
employee['net_pay'] = employee['gross_pay'] - employee['total_deductions']

print("\nEmployee Name:", employee['name'])
print("Hours Worked:", employee['hours_worked'])
print(f"Pay Rate: ${employee['hourly_rate']:.2f}")
print(f"Gross Pay: ${employee['gross_pay']:.2f}")
print("Deductions:")
print(f"  Federal Withholding ({employee['federal_tax_rate']*100:.1f}%): ${employee['federal_withholding']:.2f}")
print(f"  State Withholding ({employee['state_tax_rate']*100:.1f}%): ${employee['state_withholding']:.2f}")
print(f"  Total Deductions: ${employee['total_deductions']:.2f}")
print(f"Net Pay: ${employee['net_pay']:.2f}")



# Question 7
investment_amount = float(input("Enter the investment amount: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
years = int(input("Enter the number of years: "))

monthly_interest_rate = annual_interest_rate / 100 / 12
number_of_months = years * 12
future_investment_value = investment_amount * (1 + monthly_interest_rate) ** number_of_months

print(f"Accumulated value is ${future_investment_value:.2f}")


# Question 8
mile = float(input('Enter value in miles: '))
kilometers = mile * 1.60934
print(f"{mile} miles is {kilometers} kilometers")


