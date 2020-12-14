def is_prime(number):
  prime = True
  for i in range(2,number):
    if number % i == 0:
      prime = False

  return prime

def print_primes_between(a, b):
  for i in range(a, b):
    if is_prime(i):
      print(i)

# print(is_prime(2))
# print(is_prime(3))
# print(is_prime(10))
# print(is_prime(11))

x = int(input("Int1: "))
y = int(input("Int2: "))
print("Prime numbers between", x, "and", y)
print_primes_between(x, y)