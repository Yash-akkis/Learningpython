#Name = 'Yash'
# #Age = 36
#print("Hello" ,Name, Age)
'''
Variable_1 = int(input('Enter the value 1 :'))
Variable_2 = int(input('Enter the value 2 :'))

print(Variable_1+Variable_2)

# Using If print the value is greater than 0
if Variable_1 > 0:
    print("Value is Positive")
elif Variable_1 < 0:
    print("Value is Negative")
else:
    print("Value is Zero")
'''
'''
Requirement: Need to take 2 values from user and ask the user which type of operation want to perform. 
Perform the operation and print the operation result

x = float(input('Enter the value 1 :'))
y = float(input('Enter the value 2 :'))
Operation = input("Enter the operation to be performed : Add, Sub, Mul, Div :")

if Operation == '+':
    print(x+y)
elif Operation == '-':
    print(x-y)
elif Operation == '*':
    print(x*y)
else:
    print("None of these Operations chosen")
'''
'''
1.Requirement: Write a Python program that takes a number from the user and prints whether it is even or odd

variable = int(input('Enter the value :'))

if (variable % 2) ==0:
    print("Entered number is even")
else:
    print("Entered number is Odd")
'''

'''
Ask the user for their score (0-100), 
then convert this score into grades (A, B, C, D, E, F) using the standard grading scheme and print the result.


score = float(input('Enter the score :'))

if score >= 94:
    print('Grade A')
elif score >= 90.00 and score <= 93.99:
    print('Grade B')
elif score >= 87.00 and  score <= 89.99:
    print('Grade C')
elif score >= 84.00 and score <= 86.99:
    print('Grade D')
elif score >= 80.00  and  score <= 83.99:
    print('Grade E')
elif score <= 79.99:
    print('Grade F')
'''
'''
Based on the age input by the user, categorize them into 'Child' (< 12), 'Teen' (13-19), 'Adult' (20-64), or 'Senior' (65+)
'''
'''
age = int(input("Enter the age :"))

if age < 12:
   print(" It's a child age")
elif (13>= age <=19):
   print("It's a Teen age")
elif (20>= age <= 64):
   print("It's a adult age")
elif age > 65:
   print("It's a senior age")
'''
'''
Requirement: Create a simple calculator that takes two numbers and an operator (+, -, *, /) from the user, 
then performs the operation and prints the result.

x = float(input('Enter the value 1 :'))
y = float(input('Enter the value 2 :'))
Operation = input("Enter the operation to be performed : Add, Sub, Mul, Div :")

if Operation == '+':
    print(x+y)
elif Operation == '-':
    print(x-y)
elif Operation == '*':
    print(x*y)
elif Operation == '/':
    print(x/y)
else:
    print("None of these Operations chosen")
'''
'''
Write a program that asks the user for two numbers and prints which one is greater, or prints "Equal" if they are the same.

num1 = int(input('Enter the number1 :'))
num2 = int(input('Enter the number2 :'))

if num1 > num2:
   print('number 1 is greater than nunber 2')
elif num2 > num1:
   print('number 2 is greater than nunber 1')
else:
   print('Both the numbers are equal')
'''

'''
Requirement: Write a Python program that checks whether a year (input by the user) is a leap year or not.

Year = int(input('Enter the Year : '))

if (Year % 4 == 0):
   print(' Entered year is a Leap Year')
else:
   print("Entered year isn't a Leap Year")
'''
'''
Ask the user for coefficients a, b, and c of a quadratic equation ax^2 + bx + c = 0. Calculate and print the solutions.

a = int(input('enter the value for a'))
b = int(input('enter the value for b'))
c = int(input('enter the value for c'))
'''

'''
Write a program that takes the total shopping amount and applies a discount. 
If the amount is more than $100, apply a 10% discount; for less than $100, apply a 5% discount. Print the final price.
'''

Original_amount = float(input('Enter the shopping amount :'))

if (Original_amount > 100):
      discount = 10
      final_price = (Original_amount * discount) / 100
      print("final_prince is ")
elif (Original_amount < 100):
    discount = 5
    final_price = (Original_amount * discount) / 100
    print("final_prince is ")
