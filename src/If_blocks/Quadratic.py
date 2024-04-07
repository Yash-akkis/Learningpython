'''
Ask the user for coefficients a, b, and c of a quadratic equation ax^2 + bx + c = 0. Calculate and print the solutions.
'''
import math

a = int(input('enter the value for a :'))
b = int(input('enter the value for b :'))
c = int(input('enter the value for c :'))

if a != 0:
    print((-b+math.sqrt(b*b-4*a*c))/2*a)
    print((-b-math.sqrt(b*b-4*a*c))/2*a)