"""
Create a class "Shape", it has one instance attribute "name" and one method "fact"
which can print the string, "I am a two-dimensional shape". Make 2 classes, "Square"
and "Circle", they are both inherited from "Shape". Define functions area() in both
classes to calculate and print the areas, override the function fact() to print
"I'm a square" and "I'm a circle", respectively. Create two objects my_square and my_circle
with length 10 and radius 1, call the fact and area functions to print the results
"""

import math  # importing math library to be able to use pi later on


class Shape:  # Declaring Class called Shape
    """
    In the question, the attribute name is not initialised so to create
    an uninitialised attribute in a class, define said attribute and initialise it to none
    to avoid errors
    """
    name = None

    def fact(self):  # Declaring method fact
        print("I am a two-dimensional shape")  # Printing the string


"""
To create a class that inherits another class, in this case, Square and Circle 
inheriting Shape, pass the parent class i.e. Shape as a parameter into the respective 
child classes. For example, class Square(Shape)
"""


class Square(Shape):
    # Method to calculate area of square taking length as its parameter
    @staticmethod
    def area(length):
        return length * length

    @staticmethod
    def fact():
        print("I'm a square")  # Overriding the fat method in the parent class
        # Overriding a method means re - declaring the method but initialising it to a different value


class Circle(Shape):
    # Method to calculate area of circle taking r as its parameter
    @staticmethod
    def area(r):
        answer = math.pi * r * r
        return answer

    @staticmethod
    def fact():
        print("I'm a circle")  # Overriding the fat method in the parent class
        # Overriding a method means re - declaring the method but initialising it to a different value


my_square = Square
print(my_square.area(10))
my_square.fact()


my_circle = Circle
print(my_square.area(1))
my_circle.fact()
