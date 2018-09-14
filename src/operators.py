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

print(complex(500, 10))
# Result
# (500+10j)

real_value = 254
imaginary_value = 394

to_complex_only_real = complex(real_value)
to_complex = complex(real_value, imaginary_value)

print(to_complex_only_real)
print(to_complex)
# Result
# (254+0j)
# (254+394j)

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

int_value_1 = 69
int_value_2 = 81

int_to_character_1 = chr(int_value_1)
int_to_character_2 = chr(int_value_2)

print(int_to_character_1)
print(int_to_character_2)

# Result
# E
# Q


float_value = 56.369
long_value = 6369742212323693323265
complex_value = (214 + 254j)
tuple_value = ("John", "spy", 42)
list_value = [1, 'India', 36.45, "New Delhi"]
dict_value = {'country': 'India', 'capital': 'New Delhi'}

float_value_to_string = str(float_value)
long_value_to_string = str(long_value)
complex_value_to_string = str(complex_value)
tuple_value_to_string = str(tuple_value)
list_value_to_string = str(list_value)
dict_value_to_string = str(dict_value)

print(float_value_to_string)
print(long_value_to_string)
print(complex_value_to_string)
print(tuple_value_to_string)
print(list_value_to_string)
print(dict_value_to_string)
print()
print(float_value_to_string + long_value_to_string + complex_value_to_string +
      tuple_value_to_string + list_value_to_string + dict_value_to_string)

# Result
# 56.369
# 6369742212323693323265
# (214 + 254j)
# ('spy', 42, 'John')
# [1, 'India', 36.45, 'New Delhi']
# {'country': 'India', 'capital': 'New Delhi'}
#
# 56.3696369742212323693323265(214 + 254j)
# {'spy', 42, 'John'}[1, 'India', 36.45, 'New Delhi']
# {'country': 'India', 'capital': 'New Delhi'}


str_value = "hello"

str_to_tuple = tuple(str_value)

print(str_to_tuple)
print(str_to_tuple[0])
print(str_to_tuple[1])
print(str_to_tuple[2])
print(str_to_tuple[3])
print(str_to_tuple[4])

# Result
# ('h', 'e', 'l', 'l', 'o')
# h
# e
# l
# l
# o

str_value = "hello"

str_to_list = list(str_value)

print(str_to_list)

# Result
# ['h', 'e', 'l', 'l', 'o']


str_value = "hello Nemo!"

str_to_set = set(str_value)

print(str_to_set)

# Result
# {'h', 'o', 'l', ' ', '!', 'm', 'N', 'e'}

str_value = "hello Nemo!"

str_to_frozenset = frozenset(str_value)

print(str_to_frozenset)

# Result
# frozenset({' ', 'm', 'N', 'h', 'l', 'e', '!', 'o'})

tupils_list = z = [('1', 'a'), ('2', 'b'), ('3', 'c')]

str_to_dict = dict(tupils_list)

print(str_to_dict)

# Result
# {'1': 'a', '2': 'b', '3': 'c'}