def sum_of_nested_lists(x):
  if len(x) == 0:
    return 0
  else:
    if isinstance(x[0], list):
      return sum_of_nested_lists(x[0]) + sum_of_nested_lists(x[1:])
    else:
      return x[0] + sum_of_nested_lists(x[1:])

x = [1, 2, 3, [4, 5], [1, 1, 1, [2], [2]]]
print(sum_of_nested_lists(x))