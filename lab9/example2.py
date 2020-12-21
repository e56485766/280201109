def get_reversed(a_list):
  if len(a_list) == 0:
    return []
  else:
    return [a_list[-1]] + get_reversed(a_list[:-1])

a_list = [1, 2, 3, 4, 5, 6, 7]
print(get_reversed(a_list))