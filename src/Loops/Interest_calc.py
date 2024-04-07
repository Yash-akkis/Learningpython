'''
Implement a loop that calculates simple interest using the formula
SI = (P * R * T) / 100 where P is principal amount, R is rate per annum, and T is time in years.
The loop should ask the user for P, R, and T, calculate and print the simple interest, and
ask if they want to perform another calculation (loop until they say no).
'''

'''option1 = "yes"
option2 = "no"
user_input = input("Choose your option : ")
while True:
    p = float(input('enter the value for p: '))
    r = float(input('enter the value for r: '))
    t = float(input('enter the value for t: '))
    SI = (p * r * t) / 100
    if option1 == user_input:
        #SI = (p * r * t) / 100
        print("SI is", SI)
        break
    elif option2 == user_input:
        print(" User chosen No")
'''

option = "no"

while True:
     p = float(input('enter the value for p: '))
     r = float(input('enter the value for r: '))
     t = float(input('enter the value for t: '))
     SI = (p * r * t) / 100
     print("SI is", SI)
     user_input = input("Choose your option : ")

     if option == user_input:
         break

