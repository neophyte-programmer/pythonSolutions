"""
Create a class "Employee" and two subclasses "Manager" and "Worker". Each one has two instance
attributes "name" and "level". Every class also has a method salary(). For "Employee",
the value of salary is computed as 5000 * level. For "Manager", the value of salary is computed as
10000 * level. For "Worker", the value of salary is computed as 100 * level. Create 3 objects
(Bob:2, Cici:2, Dabby:2) and call the salary functions to print the corresponding values.
"""


class Employee:  # Creating Parent class Employee
    name = None  # Declaring attribute name and initialising it to none
    level = 0  # Declaring attribute level and initialising it to 0

    @staticmethod
    def salary(level):  # Declaring method salary() for parent class Employee
        answer = 5000 * level  # Formula to calculate salary
        return answer  # Letting the method return the result of computation


class Manager(Employee):
    @staticmethod
    def salary(level):  # Declaring method salary() for subclass Manager
        answer = 10000 * level  # Formula to calculate salary
        return answer  # Letting the method return the result of computation


class Worker(Employee):
    @staticmethod
    def salary(level):  # Declaring method salary() for subclass Worker
        answer = 1000 * level  # Formula to calculate salary
        return answer  # Letting the method return the result of computation


p1 = Employee
p1.name = "Bob"
p1.level = 2


print(p1.name + " is level " + str(p1.level) + " and his salary is " + str(p1.salary(2)) )

p2 = Manager
p2.name = "Cici"
p2.level = 2

print(p2.name + " is level " + str(p2.level) + " and his salary is " + str(p2.salary(2)) )


p3 = Worker
p3.name = "Dabby"
p3.level = 2

print(p3.name + " is level " + str(p3.level) + " and his salary is " + str(p3.salary(2)) )
