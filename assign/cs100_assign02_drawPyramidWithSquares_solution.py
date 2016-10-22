__author__ = 'Don'
import turtle


# draw Square of size x from center
def drawSquareFromCenter(turtle,x):
    turtle.penup()
    turtle.forward(-x/2)
    turtle.right(90)
    turtle.forward(x/2)
    turtle.left(90)
    turtle.pendown()
    for i in range(4):
        turtle.forward(x)
        turtle.left(90)
    turtle.penup()
    turtle.forward(x/2)
    turtle.left(90)
    turtle.forward(x/2)
    turtle.right(90)


# draw Row of numBlocks blocks with sides of length size
def drawRowWithSquares(turtle, numBlocks, size):
    for i in range(numBlocks):
        drawSquareFromCenter(turtle, size)
        turtle.forward(size)

    # put cursor back to original position and orientation
    # move cursor backward by the amount it moved forward
    turtle.forward(-size * numBlocks)


# draw Pyramid of Squares of height numBlocks with sides of length size
def drawPyramid(turtle, numBlocks, size):
    for i in range(numBlocks):
        drawRowWithSquares(turtle, numBlocks-i, size)
        turtle.left(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size / 2)

    # put cursor back to original position and orientation
    # move cursor down by the amount it moved up
    turtle.right(90)
    turtle.forward(numBlocks * size)

    # move cursor backward by the amount it moved forward
    turtle.left(90)
    turtle.forward(-(numBlocks * size) / 2)


def main():
    # Create turtle
    bob = turtle.Turtle()

    # get input from user for height of pyramid and and size of blocks
    blocks = int(input('Enter height of Pyramid (in blocks): '))
    size   = int(input('Enter size of blocks: '))
    drawPyramid(bob, blocks, size)

    # wait for user to exit
    input('Press Enter to exit')


main()
