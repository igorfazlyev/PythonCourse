#!./venv/bin/python
import random

people = ["Liam", "Olivia", "Noah", "Ava",
          "James", "Amelia", "William", "Emma"]

skills = ["coding", "art", "testing", "management", "marketing"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

people_and_skills = {person: set(random.sample(skills, 2)) for person in people}

"""
1. Randomly assign two skills to each person. Store this information in a suitable data structure
2. Write a program which prints the list of days four times, and for each day prints the names of three people who will work on that day. Also print the total set of skills from all people combined for each day.

The people should be chosen for each day in the order they are found in the people list, with no one person being chosen to work more often than any other.

"""

# Globals
# Choosing a random element from a set
# Modular counting


def main():
    index = 0
    for day in days*4:
        print(day, end=": ")
        skills_to_print=set()
        for i in range(4):
            person_to_print= people[index]
            skills_to_print.update(people_and_skills[person_to_print])
            print(person_to_print, end=" ")
            index += 1
            if index > len(people) - 1:
                index = 0
        print("combined sills: ", end=" - ")
        for skill in sorted(list(skills_to_print)):
            print(skill, end=" ")
        print()
    

main()