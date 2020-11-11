# Write a Python code that asks the user for
# a number, calculate the absolute value of
# the number and print it.

number = float(input("Number: "))

if number < 0:
    number = number * -1

print(number)