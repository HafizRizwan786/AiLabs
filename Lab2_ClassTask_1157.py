# Task 1
x=9
if x>0:
    if x>10:
        print('Large')
    print('positive')
print('Done')


x=20
if x>0:
    if x>10:
        print('Large')
    print('positive')
print('Done')


# Task 2
x='Hello World'
print(x)
x=20
print(x)
x=20.5
print(x)
x=1j
print(x)
x=['apple','bannana','cherry']
print(x)
x=('apple','bannana','cherry')
print(x)
x=range(6)
print(x)
x={'apple','bannana','cherry'}
print(x)
x=frozenset({'apple','bannana','cherry'})
print(x)
x={
    'name':'Hafiz',
    'age':18
}
print(x)
x=True
print(x)


# Task 3
age=45
salary=1456.8
name='Hafiz'
x=y=z=45
i,j,k='Orange','Bannana','Cherry'

print(age)
print('Salary',salary)
print('Name: ',name)
print(i)
print(j)
print(k)
print(f"{x} : {y} : {z}")


# Task 4
x=int(input('Enter first number : '))
y=int(input('Enter second number: ')) 
print('Sum : ',x+y)
print('Product : ',x*y)
print('Division : ',x/y)
print('Exract Division : ',x//y)


# Task 5
str='HafizRizwan'
print(str[-6:-1])
print(str[:5])
print(str[5:])



# Task 6
a=60
b=13
print('a= ',bin(a),'\nb= ',bin(b))
print('a&b= ',bin(a&b))
print('a|b= ',bin(a|b))
print('a^b= ',bin(a^b))
print('~a= ',bin(~a))
print('a<<2= ',bin(a<<2)) #Left shift
print('a>>2= ',bin(a>>2)) #right shift


# Task 7
a=10
if a%2==0:
    if a%5==0:
        print('Number is divisible by 2 and 5')


if a==11:
    print('a is 11')
elif a==10:
    print('a is 10')
else:
    print('a is not present')
    
    
# Task 8
def add(x,y,z=0):
    print('Addition is = ',x+y+z)
    

def mul(x,y,z=1):
    print('Multiplication is = ',x*y*z)

def div(x,y,z=1):
    print('Division is = ',x//y//z)

a=9
b=5
c=3

add(a,b)
mul(a,b,c)
div(a,b)
