a = "bee sting"
print(a.capitalize())
# Result
# Bee sting

a = "BEE"
print(a.casefold())
# Result
# bee

# center(width[, fillchar])
a = "bee"
b = a.center(12, "-")
print(b)

# count(sub[, start[, end]])
a = "Mushroooom soup"
print(a.count("O"))
print(a.count("o"))
print(a.count("oo"))
print(a.count("ooo"))
print(a.count("Homer"))
print(a.count("o", 4, 7))

# encode(encoding="utf-8", errors="strict")
from base64 import b64encode

a = "Banana"
print(a)

a = b64encode(a.encode())
print(a)


a = "Banana"
print(a.endswith("a"))
print(a.endswith("nana"))
print(a.endswith("z"))
print(a.endswith("an", 1, 3))

# expandtabs(tabsize=8)
a = "1\t2\t3"
print(a)
print(a.expandtabs())
print(a.expandtabs(tabsize=12))
print(a.expandtabs(tabsize=2))


a = "Fitness"
print(a.find("F"))
print(a.find("f"))
print(a.find("n"))
print(a.find("ness"))
print(a.find("ess"))
print(a.find("z"))
print(a.find("Homer"))

# format(*args, **kwargs)
# Example 1
print("{} and {}".format("Tea", "Coffee"))

# Example 2
print("{1} and {0}".format("Tea", "Coffee"))

# Example 3
print("{lunch} and {dinner}".format(lunch="Peas", dinner="Beans"))

# Example 4
print("{0}, {1}, {2}".format(*"123"))

# Example 5
lunch = {"food": "Pizza", "drink": "Wine"}
print("Lunch: {food}, {drink}".format(**lunch))


# Example 1
lunch = {"Food": "Pizza", "Drink": "Wine"}
print("Lunch: {Food}, {Drink}".format_map(lunch))

# Example 2
class Default(dict):
    def __missing__(self, key):
      return key

lunch = {"Food": "Pizza"}
print("Lunch: {Food}, {Drink}".format_map(Default(lunch)))

lunch = {"Drink": "Wine"}
print("Lunch: {Food}, {Drink}".format_map(Default(lunch)))

a = "Fitness"
print(a.index("F"))
print(a.index("n"))
print(a.index("ness"))
print(a.index("ess"))

# Like find() (above), but raises a ValueError when the substring is not found
# (find() returns -1 when the substring isn't found).
try:
    print(a.index("z"))   #Error
except ValueError as e:
    print(e)


c = "Fitness"
print(c.isalnum())

c = "123"
print(c.isalnum())

c = "1.23"
print(c.isalnum())

c = "$*%!!!"
print(c.isalnum())

c = "0.34j"
print(c.isalnum())


c = "Fitness"
print(c.isalpha())

c = "123"
print(c.isalpha())

c = "$*%!!!"
print(c.isalpha())


c = "123"
print(c.isdecimal())

c = u"\u00B2"
print(c.isdecimal())

c = "1.23"
print(c.isdecimal())

c = "u123"
print(c.isdecimal())

c = "Fitness"
print(c.isdecimal())

c = "$*%!!!"
print(c.isdecimal())


c = "123"
print(c.isdigit())

c = u"\u00B2"
print(c.isdigit())

c = "1.23"
print(c.isdigit())

c = "u123"
print(c.isdigit())

c = "Fitness"
print(c.isdigit())

c = "$*%!!!"
print(c.isdigit())


a = "123"
print(a.isidentifier())

a = "_user_123"
print(a.isidentifier())

a = "_user-123"
print(a.isidentifier())

a = "Homer"
print(a.isidentifier())

a = "for"
print(a.isidentifier())


a = " "
print(a.islower())

a = "123"
print(a.islower())

a = "_user_123"
print(a.islower())

a = "Homer"
print(a.islower())

a = "HOMER"
print(a.islower())

a = "homer"
print(a.islower())

a = "HOMER"
a = a.casefold() #Force lowercase
print(a.islower())


c = "123"
print(c.isnumeric())

c = u"\u00B2"
print(c.isnumeric())

c = "1.23"
print(c.isnumeric())

c = "u123"
print(c.isnumeric())

c = "Fitness"
print(c.isnumeric())

c = "$*%!!!"
print(c.isnumeric())


a = ""
print(a.isprintable())

a = " "
print(a.isprintable())

a = u"\u00B2"
print(a.isprintable())

a = "Bart"
print(a.isprintable())

a = "\t"
print(a.isprintable())

a = "\r\n"
print(a.isprintable())

a = "Bart \r"
print(a.isprintable())

a = ""
print(a.isspace())

a = " "
print(a.isspace())

a = "Bart"
print(a.isspace())

a = "\t"
print(a.isspace())

a = "\r\n"
print(a.isspace())

a = "Bart \r"
print(a.isspace())

a = ""
print(a.istitle())

a = " "
print(a.istitle())

a = " t"
print(a.istitle())

a = " T"
print(a.istitle())

a = "Tea"
print(a.istitle())

a = "Tea and Coffee"
print(a.istitle())

a = "Tea And Coffee"
print(a.istitle())

a = "1. Tea & Coffee \r"
print(a.istitle())


a = " "
print(a.isupper())

a = "123"
print(a.isupper())

a = "_USER_123"
print(a.isupper())

a = "Homer"
print(a.isupper())

a = "HOMER"
print(a.isupper())

a = "homer"
print(a.isupper())

a = "HOMER"
a = a.casefold() #Force lowercase
print(a.isupper())


a = "-"
print(a.join("123"))

a = "."
print(a.join("USA"))

a = ". "
print(a.join(("Dr", "Who")))

a = "bee"
b = a.ljust(12, "-")
print(b)

a = "BEE"
print(a.lower())

a = "      Bee      "
print(a.lstrip(), "!")

a = "-----Bee-----"
print(a.lstrip("-"))

frm = "SecrtCod"
to = "12345678"
trans_table = str.maketrans(frm, to)
secret_code = "Secret Code".translate(trans_table)
print(secret_code)


a = "Python-program"

print(a.partition("-"))
print(a.partition("."))


a = "Tea bag. Tea cup. Tea leaves."

print(a.replace("Tea", "Coffee"))
print(a.replace("Tea", "Coffee", 2))

a = "Yes Fitness"

print(a.rfind("Y"))
print(a.rfind("e"))
print(a.rfind("s"))
print(a.rfind("ss"))
print(a.rfind("y"))
print(a.rfind("z"))
print(a.rfind("Homer"))

a = "Yes Fitness"

try:
    print(a.rindex("Y"))
    print(a.rindex("e"))
    print(a.rindex("s"))
    print(a.rindex("ss"))
    print(a.rindex("y"))
    print(a.rindex("z"))
    print(a.rindex("Homer"))
except ValueError as e:
    print(e)

a = "bee"
b = a.rjust(12, "-")
print(b)

a = "Homer-Jay-Simpson"

print(a.rpartition("-"))
print(a.rpartition("."))

a = "Homer Jay Simpson"
print(a.rsplit())

a = "Homer-Jay-Simpson"
print(a.rsplit(sep="-",maxsplit=1))

a = "      Bee      "
print(a.rstrip(), "!")

a = "-----Bee-----"
print(a.rstrip("-"))

# split(sep=None, maxsplit=-1)
a = "Homer Jay Simpson"
print(a.split())

a = "Homer-Jay-Simpson"
print(a.split(sep="-",maxsplit=1))

a = "Homer,,Bart,"
print(a.split(","))

a = "Homer,,Bart"
print(a.split(",", maxsplit=1))

a = "Homer<>Bart<>Marge"
print(a.split("<>"))


a = "Tea\n\nand coffee\rcups\r\n"

print(a.splitlines())
print(a.splitlines(keepends=True))


a = "Homer"

print(a.startswith("H"))
print(a.startswith("h"))
print(a.startswith("Homer"))
print(a.startswith("z"))
print(a.startswith("om", 1, 3))


a = "      Bee      "
print(a.strip(), "!")

a = "-----Bee-----"
print(a.strip("-"))


a = "Homer Simpson"
print(a.swapcase())
# Result
# hOMER sIMPSON

a = "tea and coffee"
print(a.title())

a = "TEA AND COFFEE"
print(a.title())

# Result
# Tea And Coffee
# Tea And Coffee


frm = "SecrtCod"
to = "12345678"
trans_table = str.maketrans(frm, to)
secret_code = "Secret Code".translate(trans_table)
print(secret_code)

# Result
# 123425 6782


a = "bee"
print(a.upper())

a = "36"
print(a.zfill(5))

a = "-36"
print(a.zfill(5))

a = "+36"
print(a.zfill(5))

# Result
# 00036
# -0036
# +0036