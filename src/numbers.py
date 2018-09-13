# Create the number objects
a = 1
b = -1
c = 1.0
d = -1.0
e = +2e3
f = -2e3
g = 3.14j
h = -3.14j

# Print the numbers and types (we also use a 'tab' character ("\t") - just to align them)
print(type(a), "\t\t", a)
print(type(b), "\t\t", b)
print(type(c), "\t", c)
print(type(d), "\t", d)
print(type(e), "\t", e)
print(type(f), "\t", f)
print(type(g), "\t", g)
print(type(h), "\t", h)



# Import the 'random' module
import random

# Generate a floating point number between 0.0, 1.0
print(random.random())

# Generate an integer between 1 and 100
print(random.randint(1,100))

# Choose a number from the list
print(random.choice([10, 20, 30, 40, 50, 60, 70, 80, 90]))

# Take a sample of 3 numbers from the list
print(random.sample([10, 20, 30, 40, 50, 60, 70, 80, 90], 3))

# Take a sample of 5 numbers from the list
print(random.sample([10, 20, 30, 40, 50, 60, 70, 80, 90], 5))



# Using multiple parameters
print(max(1, 2, 3))
print(min(1, 2, 3))

# Using a list
a = [11, 22, 33, 44, 55, 66, 77]
print(max(a))
print(min(a))


a = 100
b = 2.5
c = a + b
print(a, type(a))
print(b, type(b))
print(c, type(c))


a = 100
print(type(a))
print(type(float(a)))
print(type(complex(a)))
print(type(bool(a)))


# Binary
print(0b11)

# Octal
print(0o15)

# Hexadecimal
print(0xe)


# Binary
print("...", 0b001, 0b010, 0b011, 0b100, 0b101, "...")

# Octal
print("...", 0o05, 0o06, 0o07, 0o10, 0o11, 0o12, 0o13, 0o14, 0o15, "...")

# Hexadecimal
print("...", 0x7, 0x8, 0x9, 0xa, 0xb, 0xc, 0xd, 0xe, 0xf, 0x10, 0x12, 0x13, "...")



a = 100
print(oct(a))
print(hex(a))