'''
Password Attempt: Create a program that sets a password string.
Ask the user to enter the password. If they enter it incorrectly, keep asking them up to 3 times.
After 3 incorrect attempts, print a failure message. If they get it right, print a success message.
'''


while True:
    password = "Password@24"
    user_input = input("Enter the password : ")
    if password == user_input:
        print("Success")
        break
    elif password != user_input:
        print("Failure")

