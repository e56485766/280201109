def hailstone(x):
  if x == 1:
    return [1]
  else:
    if x % 2 == 0:
      return [x] + hailstone(x // 2)
    else:
      return [x] +hailstone(3 * x + 1)

print(*hailstone(11), sep=", ")