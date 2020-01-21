"""
    @author Jenish Kevadia

    Script checks whether the triangle is scalene, isosceles, equilateral, or right triangle
"""

import sys

def classify_triangle(a, b, c):
    """ Check the type of triangle """

    a = check_input(a)
    b = check_input(b)
    c = check_input(c)

    x = a ** 2 + b ** 2
    y = c ** 2
    
    if a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        if x == y:
            return 'Isosceles and Right triangle'
        else:
            return 'Isosceles'
    elif a != b and b != c:
        if x == y:
            return 'Scalene and Right triangle'
        else:
            return 'Scalene'

def check_input(num):
    """ Check if the user entered input is a number or not """

    try:
        num = int(num)
        if num < 0:
            raise ValueError
    except ValueError:
        print('Input is an invalid integer')
        sys.exit(1)

    return num

def main():
    """ Get the input from the user and print the type of the triangle """

    a = input('Enter first side of the triangle: ')
    b = input('Enter second side of the triangle: ')
    c = input('Enter third side of the triangle: ')

    print(f'The triangle is: {classify_triangle(a, b, c)}')


if __name__ == '__main__':
    """ Run the main function on startup """
    main()
