### Learning the basics of creating and instantiating simple classes

## why use classes? classes are used throughout most modern programming languages 
# because they allow us to logically group our data and functions in a way thats easy
# to reuse and also easy to build upon if need be.

## data and funcitons are referred to attributes and methods.
# method = function associated with a class.

## Example problem: representing employees in our python code. This is a good use case for
# classes because each employee is going to have specific attributes and methods.
# (name, email address, pay, and actions they can preform). with classes we can create
# a blueprint or template that we can use for every employee instead of having to hard
# code a new employee every time manually. Instead, we can reference the class and
# customize its attributes for the new employee.



## Lets create a simple employee class
class Employee:
    pass # this pass statement tell python to ignore this class for now

## Class vs. Instance of a class:
#  Class = our blueprint for creating instances 
#  Instance = each unique employee that we create using our employee class will be an 
#  instance of that class.


emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)


## When printed, we see that emp_1, and emp_2 are classified as 'Employee objects' and
#  are stored at unique locations in memory.

## Instance variables contain data that is unique to each instance of a class.(emp_1, 
#  emp_2)


## we could manually define instance variables like this:
emp_1.first = 'John'
emp_1.last = 'Doe'
emp_1.email = 'John.Doe@company.com'
emp_1.pay = 50000

emp_2.first = 'Jane'
emp_2.last = 'Day'
emp_2.email = 'Jane.Day@company.com'
emp_2.pay = 150000

print()
print(emp_1.email)
print(emp_2.email)


## Let's say that we wanted to set all of these things for each employee immediately when
#  theyre created without having to define all of these things every time we create a 
#  new employee instance.


## we could do that like this
class Employee:
    
    def __init__(self, first, last, pay): # when we create methods within a class they recieve the instance as its first argument (self)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        

## having self be the first argument passed (the instance), serves the same purpose
#  as when we defined all of those variables manually earlier.

## by using this method we save ourselves from writing so much code, at the same time
#  reducing our chances of typos or errors and improving the reusability of our classes
#  this method allows us to get the most out of using classes.


## now lets create some employee objects 
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Day', 150000)

print()
print(emp_1)
print(emp_2)

print()
print(emp_1.email) 
print(emp_2.email)

print()
print(emp_1.first, emp_1.last)
print(emp_2.first, emp_2.last)


## when we create class objects this way, the instance (self) 
# is automatically passed and we dont need to include it 

## lets look at adding some methods now. lets say we want to print the employees
#  first and last name. there are a few ways to do it. one way is shown in the 
#  example above and i will show two more now


## manual method
print()
print('{} {}'.format(emp_1.first, emp_1.last))

## the second method is by defining a new method called fullname() in our class like this
class Employee:
    
    def __init__(self, first, last, pay): # when we create methods within a class they recieve the instance as its first argument (self)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    
## we only need to pass the instance (self as an argument).
#  this is the same thing we did in the manual example except we changed the 'emp_1'
#  to self because we are going to pass the specific instance when we call the 
#  function. this will make this function usable by all instances


## lets create the instances again for this new example class
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Day', 150000)

## example usage of fullname():
print()
print(emp_1.fullname())


## we need to include the parenthesis when we call fullname() because it is a method 
#  (function), not an attribute. This can be used for any instance of this Employee class


## this is what will happen if you dont use the ()
print()
print(emp_1.fullname)
#  it will return the method name and some info about its class 

## we can also call a method by using the class name directly and passing in the instance
#  argument (self). like this
print()
print(Employee.fullname(emp_2))



## I am taking Harvard CS50's AI with python course and they are working with classes so
#  i decided to learn more about them and start taking an object oriented programming 
#  course to improve my understanding and proficiency in python. 