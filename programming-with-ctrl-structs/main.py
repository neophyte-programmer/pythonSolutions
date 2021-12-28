"""
Develop a Python program which inputs a series of integers and processes them. The program will:
a) Continue to process values until the user enters the value 0
b) Ignore all negative integers
c) Count the number of odd integers entered
d) Count the number of even integers entered
e) Calculate the sum of the odd integers in the series
f) Calculate the sum of the even integers in the series
g) Display the sum of odds
h) Display the sum of evens
i) Display the count of odds
j) Display the count of evens
k) Display the total number of positive integers entered
l) BONUS: print a message whenever a negative integer is entered

"""
# this variable will store all the user input. It is initialised to None because of the while loop
# it will be re-initialised after each input
userInput = None
# this variable will store the sum of all the odd numbers that have been entered
oddSum = 0
# this variable will increase by one when an odd number is entered
oddCount = 0
# this variable will store the sum of all the even numbers that have been entered
evenSum = 0
# this variable will increase by one when an even number is entered
evenCount = 0

while userInput != 0:   # this means once the number entered is not 0 (since 0 terminates the loop)
    userInput = int(input("Enter a number: "))  # getting input from the user and casting it to int because input is
    # taken as a string so it has to be casted to int so we can work with it
    if userInput > 0:
        if userInput % 2 == 0:  # checking if the input is even
            evenSum += userInput    # if it is even, the number should be added to the evenSum variable
            evenCount += 1  # if the number is even, the evenCount should be incremented by one to count it
        elif userInput % 2 != 0:
            oddSum += userInput
            oddCount += 1

# Here we are just printing the variables
print(f"Even numbers: {evenCount} and Sum: {evenSum}")
print(f"Odd numbers: {oddCount} and Sum: {oddSum}")
