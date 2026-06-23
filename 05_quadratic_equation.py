# Solve the quadratic equation ax**2 + bx + c = 0
import cmath

a = 1
b = 5
c = 6
# calculate the discriminant
d = (b**2) - (4*a*c)
# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print(f"The solutions are {sol1} and {sol2}")
