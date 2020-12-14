def sum_of_list(a_list):
  sum = 0
  for i in a_list:
    sum += i
    return sum

list_1 = [12, -7, 5, -89.4, 3, 27, 56, 57.3]

print(sum_of_list(list_1))