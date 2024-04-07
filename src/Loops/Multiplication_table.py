'''
Write a program that prints the multiplication table of a given number.
The program should take a number from the user and print its multiplication table up to 10.
'''

user = int(input('enter the value :'))
i = 1
while i <= 10:
    print(user, '*', i, '=', user*i)
    i = i+1

