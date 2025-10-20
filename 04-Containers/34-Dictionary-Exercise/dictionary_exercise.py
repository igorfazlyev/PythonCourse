#!./venv/bin/python


"""
Write a program that asks the user to enter a name.

If the user enters a name in the list below, respond with the age
of the person entered. Otherwise print "Unknown person"

Make the program keep asking for names like this until the user enters
"quit". Then the program exits.

Start by putting the names and ages in a dictionary.
"""

def main():
    people = ["Amelia", "Arthur", "Isla", "Noah", "Ava", "Leo", "Mia", "Oscar"]
    ages = [20, 30, 25, 65, 21, 70, 32, 45]
    db = dict(zip(people, ages))
    while True:
        user_input = input("enter the name of the person whose age you want to know or q to quit: ")
        if user_input.lower() == "q":
            print("see ya")
            break
        age = db.get(user_input,"unknown person")
        if age == "unknown person":
            print(age)
        else:
            print(f"{user_input}'s {age} years old")
  
main()