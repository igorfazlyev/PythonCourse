# The Fridge

"""

Get the user to enter a temperature in celsius.

< 0: Print "Fridge too cold"
0 - 4: Print "Fridge OK"
4 - 6: Print "Fridge too warm"
> 6: Print "Fridge broken"

"""
temp = int(input("enter temperature in celsius: "))
if temp < 0:
    print("Fridge too cold")
elif temp >= 0 and temp < 4:
    print("Fridge ok")
elif temp >= 4 and temp < 6:
    print('Frdige ok')
else:
    print("Fridge broken")