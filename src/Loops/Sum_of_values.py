'''
Ask the user to input numbers continuously.
Add these numbers to a total sum. The loop should terminate when the user inputs 0, and then print the total sum.
'''

sum1 = 0

while True:
    user = int(input('Enter the number'))
    if user == 0:
        break
    else:
        sum1 = sum1+user

print('sum1 :', sum1)
