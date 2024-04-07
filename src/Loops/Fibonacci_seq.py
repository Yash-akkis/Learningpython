'''
Fibonacci Sequence: Write a program that generates the Fibonacci sequence up to a number n provided by the user.
The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
'''

num = int(input('enter the number :'))
num1 = 0
num2 = 1

fib_seq = [num1,num2]
while num2 < num:
    print("before logic", num1, num2)
    num1, num2 = num2, num1+num2
    print("after logic", num1, num2)
    fib_seq.append(num2)

print("fib sequence of the num",num, ':', fib_seq)
