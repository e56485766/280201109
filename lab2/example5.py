# Write a program that asks the user for the
# length of perpendicular edges of a right
# triangle, then calculates the hypotenuse
# and prints it.

edge1 = int(input("Edge1: "))
edge2 = int(input("Edge2: "))

hypotenuse = (edge1 ** 2 + edge2 ** 2) ** (1/2)
print(hypotenuse)