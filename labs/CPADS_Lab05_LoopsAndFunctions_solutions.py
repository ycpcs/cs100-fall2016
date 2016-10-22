__author__ = 'djhake2'

from math import *


# function that prints the integers from 0 to n - 1
def printIntegers(n):
    print("Function: printIntegers")
    for i in range(n):
        print(i)


# function that prints the first 'n' non-negative even integers
def printEvenIntegers(n):
    print("Function: printEvenIntegers")
    for i in range(n):
        print(i * 2)


# TODO 2A: create a function that outputs the first 'n' positive odd integers
def printOddIntegers(n):
    print("Function: printOddIntegers")
    for i in range(n):
        print((i * 2) + 1)


# TODO 3A: create a function that outputs the sum of the first 'n'
#          positive odd integers
def printSumOddIntegers(n):
    print("Function: printSumOddIntegers")
    sum = 0
    for i in range(n):
        sum = sum + ((i * 2) - 1)
    print(sum)


def printSquares(n):
    print("Function: printSquares")
    for i in range(n):
        print(i**2)


# TODO 4A: create a function that outputs the sum of the first 'n'
#          squares (from 0 to n - 1)
def printSumSquares(n):
    print("Function: printSumSquares")

    sum = 0
    for i in range(n):
        sum = sum + n**2
    print(sum)


# TODO 6A: create a function that outputs the cubes for 0 to n - 1
def printCubes(n):
    print("Function: printCubes")
    for i in range(n):
        print(i**3)


#  function that calculates the quadratic equation and returns the result
def calcQuadratic(a, b, c, x):
    return a* x**2 + b * x + c


# TODO 8A: create a function that calculates the cubic equation and returns the result
def calcCubic(a, b, c, d, x):
    return a* x**3 + b * x**2 + c * x + d


# function that calculates and returns the distance between 2 points in the x-y plane
def calcXYDistance(x1, y1, x2, y2):
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


# TODO 9A: create a function that calculates and returns the distance between
#          two points in the (x, y, z) space
def calcXYZDistance(x1, y1, z1, x2, y2, z2):
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance


# this is the main program, that executes when main() is called later
def main():

    # prompt user for input
    val  = int(input("Enter an integer (0-10): "))

    # this loop outputs 0 to val - 1
    print("Integers from 0 to", val -1)
    for i in range (val):
        print(i)

    input("Press any key to continue")
    # this function call does the same thing as the above loop
    printIntegers(val)

    input("Press any key to continue")
    # this loop outputs the first 'val' even integers
    print("First", val, "even integers")
    for i in range(val):
        print(2 * i)

    input("Press any key to continue")
    # this function call does the same thing as the above loop
    printEvenIntegers(val)

    input("Press any key to continue")
    # TODO 1: copy the above for loop here and modify it to output
    #       the first 'val' positive odd integers
    print("First", val, "odd integers")
    for i in range(val):
        print((2 * i) + 1)

    input("Press any key to continue")
    # TODO 2: call the function from TODO 2A that does the same thing as the above loop
    printOddIntegers(val)

    input("Press any key to continue")
    # TODO 3: call the function from TODO 3A that outputs the sum of the
    #         first 'n' positive odd integers
    printOddIntegers(val)

    input("Press any key to continue")
    print("Calculating powers")

    # this loop outputs the squares for 0 to val - 1
    for i in range(val):
        print(i**2)

    # this function call does the same thing as the above loop
    printSquares(val)

    # TODO 4: call the function from TODO 4A that outputs the sum of the
    #         first 'n' squares (from 0 to val - 1)
    printSquares(val)

    # TODO 5: copy the above loop for squares here and modify it to output
    #         the cubes for 0 to val - 1
    print("First ", val, " cubes for 0 to val -1")
    # this loop outputs the cubes for 0 to val - 1
    for i in range(val):
        print(i**3)

    # TODO 6: call the function from TODO 6A that outputs the
    #         'n' cubes for 0 to val - 1
    printCubes(val)

    input("Press any key to continue")
    print("Calculating polynomial equations")

    # get coefficients for a polynomial equation
    # the coefficients can be floating point #'s
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    d = float(input("Enter coefficient d: "))

    # x is an integer
    x = int(input("Enter integer value for x: "))

    # this code calculates the quadratic equation:
    #     ax**2 + bx + c
    # for the above inputs
    result = a*x**2 + b*x + c
    print("Quadratic Result(loop): ", result)

    # this function call does the same thing, it calculates
    # the quadratic equation and returns the result
    result = calcQuadratic(a, b, c, x)
    print("Quadratic Result(result): ", result)

    # the same thing can be accomplished by printing the return
    # value of the function directly from the print instruction
    print("Quadratic Result(function): ", calcQuadratic(a, b, c, x))

    # TODO 7: create a for loop that outputs the quadratic results for x from 0 to 10
    print("Results for Quadratic equation for x from 0 to 10")
    for i in range(11):
        y = calcQuadratic(a, b, c, i)
        print(y)

    # TODO 8: call the function from TODO 8A that calculates the cubic equation:
    #      ax**3 + bx**2 + cx + d
    # and then output the result
    y = calcCubic(a, b, c, d, x)
    print(y)

    input("Press any key to continue")
    print("Calculating distance between 2 points")

    # input the coordinates for two 3-dimensional points
    # these are the (x, y, z) values for point 1
    px1 = float(input("Enter x value for first point:  "))
    py1 = float(input("Enter y value for first point:  "))
    pz1 = float(input("Enter z value for first point:  "))

   # these are the (x, y, x) values for point 2
    px2 = float(input("Enter x value for second point: "))
    py2 = float(input("Enter y value for second point: "))
    pz2 = float(input("Enter z value for second point: "))

    # this function call returns the distance between the two points in the x-y plane
    distance = calcXYDistance(px1, py1, px2, py2)
    print("Distance(2D): ", distance)

    # TODO 9: call the function from TODO 9A that calculates the distance between
    #       two points in the (x, y, z) space and then output the result
    distance = calcXYZDistance(px1, py1, pz1, px2, py2, pz2)
    print("Distance(3D): ", distance)
    input("Press any key to exit")


main()