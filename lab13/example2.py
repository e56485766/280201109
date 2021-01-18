def binary_search(a_list, target, start, end):
  if end - start + 1 <= 0:
    return -1
  else:
    mid = start + (end - start) // 2
    if a_list[mid] == target:
      return mid
    else:
      if target < a_list[mid]:
        return binary_search(a_list, target, start, mid - 1)
      else:
        return binary_search(a_list ,target, mid + 1, end)

nums = [2, 3, 4, 15, 40, 100, 200]
print(binary_search(nums, 200, 0, len(nums)))