# Write a Python code that asks the user for
# three numbers, calculate the minimum of
# them and print it.

numbers = []

for i in range(3):
    numbers.append(input("Number " + str(i+1) + ": "))

numbers.sort()
print(numbers[0])