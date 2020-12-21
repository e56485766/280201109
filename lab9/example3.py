def get_evens(a_list):
  if len(a_list) == 0:
    return 0
  else:
    return (a_list[-1] % 2 == 0) + (get_evens(a_list[:-1]))


a_list = [-53, -10, -2, 0, 1, 2, 3, 4, 5, 6]
print(get_evens(a_list))