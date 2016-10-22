__author__ = 'Don'
import turtle
from math import *


# draw equilateral Triangle with sides of length size
# filling in triangle with blue
def drawEquiTriangleFromCenter(turtle, size):
    # find height of equilateral triangle
    # using pythagorean theorem
    height = sqrt(size**2 - (size / 2)**2)

    # position cursor to outside corner
    turtle.penup()
    turtle.forward(-size / 2)
    turtle.right(90)
    turtle.forward(height / 2)
    turtle.left(90)
    turtle.color("blue")
    turtle.begin_fill()
    turtle.pendown()

    # draw triangle, 3 sides of equal length
    # turning 120 degrees left after each side is drawn
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)

    turtle.end_fill()
    turtle.penup()

    # put cursor back to original position and orientation
    # move cursor forward about amount it moved back
    turtle.forward(size / 2)

    # move cursor up by the amount it moved down
    turtle.left(90)
    turtle.forward(height / 2)
    turtle.right(90)

    # put pen color back to black
    turtle.color("black")


# draw Row of numBlocks equilateral Triangles with sides of length size
def drawRowWithEquiTriangles(turtle, numBlocks, size):
    for i in range(numBlocks):
        drawEquiTriangleFromCenter(turtle, size)
        turtle.forward(size)

    # put cursor back to original position and orientation
    # move cursor backward by the amount it moved forward
    turtle.forward(-size * numBlocks)


# draw Pyramid of equilateral Triangles of height numBlocks with sides of length size
def drawPyramidWithEquiTriangles(turtle, numBlocks, size):

    # find height of equilateral triangle
    # using pythagorean theorem
    height = sqrt(size**2 - (size / 2)**2)

    for i in range(numBlocks):
        drawRowWithEquiTriangles(turtle, numBlocks - i, size)
        turtle.forward(size / 2)
        turtle.left(90)
        turtle.forward(height)
        turtle.right(90)

    # put cursor back to original position and orientation
    # move cursor down by the amount it moved up
    turtle.right(90)
    turtle.forward(numBlocks * height)

    # move cursor backward by the amount it moved forward
    turtle.left(90)
    turtle.forward(-numBlocks * size / 2)


def main():
    # Create turtle
    bob = turtle.Turtle()

    # get input from user for height of pyramid and and size of blocks
    blocks = int(input('Enter height of Pyramid in blocks: '))
    size   = int(input('Enter length of side of triangle: '))
    drawPyramidWithEquiTriangles(bob, blocks, size)

    # wait for user to exit
    input('Press Enter to exit')

main()
