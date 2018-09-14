# Import the 'namedtuple' function from the 'collections' module
from collections import namedtuple

# Function to perform the four basic arithmetic operations
# against two numbers that are passed in as arguments.
def basicArithmetic(x, y):

    # Do the calulations and put each result into a variable
    sum = x + y
    product = x * y
    quotient = x / y
    difference = x - y

    # Create named tuple
    result = namedtuple("Result", "sum product quotient difference")
    thisResult = result(sum, product, quotient, difference)

    # Return variable
    return thisResult

# Function to multiply a number by itself
def multiplyMe(x):
    y = x * x
    return y