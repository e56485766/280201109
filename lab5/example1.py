integer = int(input("Enter an integer: "))

for i in range(10):
  multi = integer
  multi *= (i+1)
  print(integer,"x", i+1, "=", multi)