import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b - math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return "No real roots"

# Directly passing values for a, b, and c
a = 1
b = -3
c = 2

roots = solve_quadratic(a, b, c)
print(f"The roots of the quadratic equation are: {roots}")
