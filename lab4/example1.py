num = input("Number: ")

if len(num) == 1 or (int(num) < 0 and len(num) == 2):
    sum = int(num[len(num)-1])
else:
    sum = int(num[len(num)-1]) + int(num[len(num)-2])

print(sum)