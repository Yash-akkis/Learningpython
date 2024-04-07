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
