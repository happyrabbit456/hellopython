import random
print(random.randint(1,100))

randint = random.randint
print(randint(1,100))

# Import the functions from the 'calculations' module
from src.calculations import basicArithmetic, multiplyMe

# Call the 'multiplyMe' function and print the result
print(multiplyMe(894758))

# Call the 'basicArithmetic' function and assign its value to a variable
calculation = basicArithmetic(325,987)
# Print each result separately
print(calculation.sum)
print(calculation.product)
print(calculation.quotient)
print(calculation.difference)


# Option 1
import src
from src import calculations
print(calculations.multiplyMe(10))

# Option 2
import src.calculations
print(src.calculations.multiplyMe(10))

# Option 3
from src import calculations
print(calculations.multiplyMe(10))

# Option 4
from src.calculations import multiplyMe
print(multiplyMe(10))

# Option 5
from src.calculations import *
print(multiplyMe(10))