'''
Odd Numbers Printer: Write a program that asks the user for two numbers, start and end.
Using a while loop, print all odd numbers between start and end (inclusive).
'''

start = int(input('Enter the starting num : '))
end = int(input('Enter the ending num : '))

while start <= end:
    if start %2 != 0:
        print(start)
    start = start+1


