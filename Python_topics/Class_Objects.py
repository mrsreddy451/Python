
'''

#class creation
class Student:
#Pass means empty class
    pass

#Create instance/object of class
std_1 = Student()
std_2 = Student()

std_1.first ="raja"
std_1.last = "Moola"
std_1.email ="raja@gmail.com"
std_1.marks = 70


std_2.first ="rajasekhar"
std_2.last = "ReddyMoola"
std_2.email ="rajasekhar@gmail.com"
std_2.marks = 90


print(std_1.email)
print(std_2.email)

'''

'''
#Above code, can be write by writing methdd inside calss .
#this can be call as constructor in java. it calls self when the instance created for that class.
class Student:

    Mp = 1.05
    def __init__(self, first, last, marks) :
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + '.'+last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def marks_rise(self):
        #global Mp
        self.marks = int(self.marks) * 1.05

std_1 = Student("raja",'moola',70)
std_2 = Student('Raja Sekhar','Reddy Moola',90)

print(std_1.first)
print(std_2.first)
print(std_2.email)
print(std_1.email)  
print(std_1.marks)
print(std_1.fullname())
print(std_1.marks_rise())
print(std_1.__dict__)
'''

'''
#Below code is for the example of inheritance in Python.
class Student:

    Mp = 1.05
    def __init__(self, first, last, marks) :
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + '.'+last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def marks_rise(self):
        #global Mp
        self.marks = int(self.marks) * 1.05
#Inherit the class Student
class dumb(Student):
    perc_raise = 1.10

    def __init__(self, first, last, marks, prog_lang):
        #inorder to avoid the code re-write,we have an option called super() function to get the base class code.
        super().__init__(first,last,marks)
        self.prog_lang = prog_lang

std_1 = dumb("raja",'moola',70,'Python')
print(std_1.prog_lang)
std_2 = Student('Raja Sekhar','Reddy Moola',90)
#print(help(dumb)) # to know flow of execusion from sub class to base class.
'''

'''
#Abstact Classes 
-> Abstract class can not be instantiated.means, can not create objects/instaces for these classes. 
-> It can only be inherited.
-> We need to call the abstract methodes at least once in the sub class
'''
from abc import ABC, abstractmethod
class Employee():
    @abstractmethod

    def cal_sal(self):
        pass

emp2 = Employee()
emp2.sal = 1000

print(emp2.sal)

class Developer(Employee):
    def cal_sal(self, sal):
        final_sal = sal * 1.10
        return final_sal

    def position(self, position):
        self.position = position
        return position


emp1 = Developer()

#print(emp1.cal_sal(1000))

print(emp1.position('developper'))