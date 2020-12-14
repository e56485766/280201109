def is_prime(number):
  prime = True
  for i in range(2,number):
    if number % i == 0:
      prime = False

  return prime
        
print(is_prime(2))
print(is_prime(3))
print(is_prime(10))
print(is_prime(11))