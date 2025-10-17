#!./venv/bin/python

"""
Write a function that asks the user to enter their weight in kilos
and their height in metres, then calculatues their BMI

(weight divided by height times height)

The function should return all three values.
"""

def main():
    weight, height, bmi = body_mass_index()
    print(f"Your weight is {weight}kg\nYour height is {height}m\nYour bmi is {bmi}")


def body_mass_index():
    weight = float(input("enter youwr weight in kilos: "))
    height = float(input("enter your heigh in meters: "))
    return weight, height, weight/height**2 

main()
