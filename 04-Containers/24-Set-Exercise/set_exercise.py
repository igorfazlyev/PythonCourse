#!./venv/bin/python

"""
Print all the cubic numbers up to and including 729
Print all the square numbers up to and including 729

Which cubic numbers are also square numbers?
Which cubic numbers are not square numbers?
"""

def main():
    cubes = {x * x * x for x in range(1, 10)}
    print(sorted(list(cubes)))
    squares = {x * x for x in range(1, 28)}
    print(sorted(list(squares)))
    print("cubes that are also squares: ", cubes.intersection(squares))
    print("cubes that are not squares: ", cubes.difference(squares))
main()
