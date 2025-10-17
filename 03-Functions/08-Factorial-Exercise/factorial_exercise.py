#!./venv/bin/python

"""
Write a function that calculates the factorial of a number.

The factorial of a number is defined like this:

n! = n * (n - 1) (n - 2) * ... * 3 * 2 * 1

e.g. 

3! = 3 * 2 * 1
5! = 5 * 4 * 3 * 2 * 1

The factorial of zero, 0!, is defined as 1.

Calcuate the factorial of 7 , i.e. 7!

Hint:

Use a loop
Create a variable before the loop, and have the
loop repeatedly alter the number that the variable
refers to.

"""
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)

def main():
    num = int(input("Enter a number to find the factorial of: "))
    print(f"the factorial of {num} is {factorial(num)}")
    
main()
