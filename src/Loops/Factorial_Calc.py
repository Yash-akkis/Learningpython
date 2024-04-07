'''
Factorial Calculator: Write a Python program that calculates the factorial of a given number.
The factorial of a number n is the product of all positive integers less than or equal to n.
'''
user_input = int(input('Enter the num for factorial :'))
fact = 1
while user_input > 0:

    fact = fact*user_input
    user_input = user_input-1

print(fact)
