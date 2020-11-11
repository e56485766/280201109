# Write a Python code that asks the user for
# parameters(a, b, c) of a quadratic equation
# represented as: ax^2 + bx + c. The code should
# calculate & print out the roots accordingly.

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

discriminant = b ** 2 - 4 * a * c

root1 = (b * -1 + (b ** 2 - 4 * a * c)**(1/2)) / (2 * a)
root2 = (b * -1 - (b ** 2 - 4 * a * c)**(1/2)) / (2 * a)

if discriminant > 0:
    print("Two Real Roots: ", root1, root2)
elif discriminant == 0:
    print("One Real Root: ", root1)
else:
    print("Two Complex Roots: ", root1, root2)
