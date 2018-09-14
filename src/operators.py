print(500 + 20)
print(500 - 20)
print(500 * 20)
print(500 / 20)
print(500 // 20)
print(500 % 20)
print(20 ** 50)

print(1==1)
print(1==2)

print(1==1 and 2==2)
print(1==1 and 1==2)

a = 10
b = 20
a = a + b
print(a)

a = 10
b = 20
a += b
print(a)

print(500 | 200)


a = 7
print("Low" if a < 10 else "High")

print(abs(-500))
# Result
# 500

print(int(500.26))
# Result
# 500

print(float(500))
# Result
# 500.0

print(complex(500, 10j))
# Result
# (490+0j)

c = 3+4j
print(c.conjugate())
# Result
# (3-4j)

# divmod(x, y)
# The pair (x // y, x % y)
print(divmod(94, 21))
# Result
# (4, 10)

print(pow(500, 2))
# Result
# 250000

print(500 ** 2)
# Result
# 250000


import math
x = 123.56
print(math.trunc(x))
# Result
# 123

# round(x[, n])
# x rounded to n digits, rounding half to even. If n is omitted, it defaults to 0.
x = 123.56
# print(math.round(x, 1)) //error: module 'math' has no attribute 'round'
print(round(x, 1))
# Result
# 123.6

import math
x = 123.56
print(math.floor(x))
# Result
# 123

import math
x = 123.56
print(math.ceil(x))
# Result
# 124