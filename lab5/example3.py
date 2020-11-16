n1 = input("Enter number 1:")[::-1]
n2 = input("Enter number 2:")[::-1]

match = 0

if int(n1) >= int(n2):
  control = n2
else:
  control = n1

for i in range(0,len(control)-1):
  if n1[i] == n2[i]:
    match += 1

print(match)