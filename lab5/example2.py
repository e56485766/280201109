n = int(input("How many numbers? "))

even = 0

for i in range(n):
  number = int(input("Enter an integer: "))
  if number % 2 == 0:
    even += 1

percentage = even / n * 100
print(str(percentage) + "%")