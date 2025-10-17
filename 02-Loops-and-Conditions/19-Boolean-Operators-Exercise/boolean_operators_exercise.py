#!./venv/bin/python

"""
Write a program that asks the user three questions.

Ask the user:
1. Are you a student?
2. Do you have pets?
3. Do you smoke?

The program automatically decides whether a property you've applied to rent is available to you.

It should print an appropriate response, like "Property available" or "Property unavailable".

The program applies these criteria:

If you're a student, you can only rent the property if you don't have pets and don't smoke.

If you're not a student, you can rent the property if you smoke or have pets, but not if you
both smoke and also have pets.



"""
student = input("Are you a student? y/n: ").lower() == 'y' 
pets = input("Do you have pets? y/n: ").lower() == 'y'
smoke = input("Do you smoke? y/n: ").lower() == 'y' 

YES_MESSAGE = "Property available"
NO_MESSAGE = "Property unavailable"

available = (student and not pets and not smoke) or (not student and not (pets and smoke ))
if available:
    print(YES_MESSAGE)
else:
    print(NO_MESSAGE)