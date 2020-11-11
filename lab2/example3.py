# Write a program to find roots of the following
# quadratic equation.

a = 2
b = 6
c = -20

root1 = (b * -1 + (b ** 2 - 4 * a * c)**(1/2)) / (2 * a)
root2 = (b * -1 - (b ** 2 - 4 * a * c)**(1/2)) / (2 * a)

print(root1, "and", root2)