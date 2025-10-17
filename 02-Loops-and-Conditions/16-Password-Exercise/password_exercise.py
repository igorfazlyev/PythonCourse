#!./venv/bin/python

"""

Write a program that asks the user to enter a password and compares it to a hard-coded password.

If the password is correct, the program prints "Greetings Professor Falcon" and exits.

If the password is incorrect, the program prints "Access denied" and then asks for the password again.

The program will ask for the password three times if necessary.

After that, it exits.

"""
PASSWORD ="#M9078q"
GREETING = "Greetings Professor Falcon"
DENIED_MESSAGE = "Access denied"

for _ in range(3):
    user_entered_pwd = input("enter your password: ")
    if user_entered_pwd == PASSWORD:
        print(GREETING)
        break
    else:
        print(DENIED_MESSAGE)
