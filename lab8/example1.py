def sum_of_list(numbers):
  value = 0
  
  for i in numbers:
    value += i

  return value ** 2

a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
value = sum_of_list(a_list)
print(value)