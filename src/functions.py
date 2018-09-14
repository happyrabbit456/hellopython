def multiplyMe(x):
    y = x * x
    return y

print(multiplyMe(10))
a = multiplyMe(10)
b = multiplyMe(15)
c = a + b
print(c)

# Function to perform the four basic arithmetic operations
# against two numbers that are passed in as arguments.
def basicArithmetic(x, y):

    # Do the calulations and put each result into a variable
    sum = x + y
    product = x * y
    quotient = x / y
    difference = x - y

    # Return each variable
    return sum, product, quotient, difference


# Call the function and print the result
print(basicArithmetic(3, 30))

# Call the function and print the result
print(basicArithmetic(3,30)[0])
print(basicArithmetic(3,30)[1])
print(basicArithmetic(3,30)[2])
print(basicArithmetic(3,30)[3])


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


# Call the function and assign its value to a variable
calculation = basicArithmetic(3,30)

# Print each result separately
print(calculation.sum)
print(calculation.product)
print(calculation.quotient)
print(calculation.difference)