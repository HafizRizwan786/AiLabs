# Task 1
"""
class Add:
    def __init__(self,a):
        self.a=a
    
    def __add__(self, other):
        return self.a+other.a
    
ob1=Add(1.5)
ob2=Add(22.6)
ob3=Add("Hafiz")
ob4=Add("Rizwan")
print(ob1+ob2)
print(ob3+ob4)



# Task 2
class Person:
    def __init__(self,fname,Iname):
        self.fname=fname
        self.Iname=Iname
        
    def printname(self):
        print(self.fname+self.Iname)
        
class Student(Person):
    pass

x=Student("Muhammad",'Rizwan')
x.printname()



# Task 3
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        
    def printname(self):
        print(self.fname,self.lname)
        
class Student(Person):
    def __init__(self, fname, lname,graduationyear):
        super().__init__(fname, lname)
        self.graduationyear=graduationyear
        
    def welcome(self):
        print(f"Welcome {self.fname} {self.lname} to the class of {self.graduationyear}")
        
x=Student('Hafiz','Rizwan',2026)
x.printname()
x.welcome()


"""
# Task 4
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        
    def printname(self):
        print(f"Person Name: {self.fname} {self.lname}")
        
class Student(Person):
    def __init__(self, fname, lname,graduationyear):
        super().__init__(fname, lname)
        self.graduationyear=graduationyear
        
    def welcome(self):
        super().printname()
        print(f"Student Graduation Year: {self.graduationyear}")
        
x=Student('Hafiz','Rizwan',2026)
x.welcome()



# Self Learning
# class Student:
#     def __init__(self, name, marks, roll):
#         self.name = name
#         self.marks = marks
#         self.roll = roll

#     def __add__(self, other):
#         combined_name = f"{self.name} & {other.name}"
#         combined_roll = self.roll
#         return Student(combined_name, self.marks + other.marks, combined_roll)


# s1 = Student("Ali", 80, 101)
# s2 = Student("Ahmed", 90, 202)
# s3 = Student("Sara", 70, 303)

# result = s1 + s2 + s3
# print(f"{result.name} | {result.marks} | {result.roll}")
