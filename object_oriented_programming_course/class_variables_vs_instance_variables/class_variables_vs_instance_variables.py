# In this lesson we look at the difference between class variables and instance variables

class Employee:
    
    num_of_employees = 0
    raise_amount = 1.04 # class variable
    
    def __init__(self, first, last, pay):
        
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_employees += 1 # every time we initialize a new employee, the 
                                       # employee count goes up by one.
    
    def fullname(self):
        
        return '{} {}'.format(self.first, self.last)
    
    def give_raise(self,):
        
        self.pay = self.pay * self.raise_amount # if we change this to Employee.raise_amount
                                                # we will be accessing the raise amount stored
                                                # in the class name space, whereas if we leave
                                                # it as self.raise_amount we can use the value
                                                # stored in the name space of the specific 
                                                # instance we choose which can be changed as 
                                                # shoen below.
                                    
    
# initialize/instantiate 2 employees
emp_1 = Employee('Sky', 'Jackson', 30000)
emp_2 = Employee('Alex', 'Jones', 0)

# give a raise to a specific employee/instance
print(emp_1.pay)
emp_1.give_raise()
print(emp_1.pay)

# class variable
print()
print(emp_1.raise_amount)
print(Employee.raise_amount)

# print name space
print()
print(emp_1.__dict__)
print()
print(Employee.__dict__)

# changing class variable for the class and all instances
print()
Employee.raise_amount = 1.10
print(Employee.raise_amount)

# changing class variable for only one instance 
print()
emp_1.raise_amount = 1.50
print(emp_1.raise_amount)
print(Employee.raise_amount)

print()
print(emp_1.__dict__)

print()
emp_1.give_raise()
print(emp_1.__dict__)

# print number of employees intialized/instantiated
print()
print(Employee.num_of_employees) # this will be two because we have only created 2 so far 

emp_3 = Employee('Flying', 'Dutchman', 1000000)

print()
print(Employee.num_of_employees) # now it will be 3



## you can change class variables for the whole class and all instances or you can change
#  them for only specific instances as demonstrated above. methods will access the values
#  stored in the specified namespace (Class or specific instance) which can differ from
#  eachother.