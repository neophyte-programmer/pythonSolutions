# Given a 6 digit integer, find the first 3, last 2 and middle 2 digits

x_str = input("Input x: ")
x_int = int(x_str)

first_three = x_int // 1000
last_two = x_int % 100
middle_two = x_int % 10000
middle_two = middle_two // 100


print("original input: " + str(x_str))
print("first_three: " + str(first_three))
print("last_two: " + str(last_two))
print("middle_two: " + str(middle_two))
