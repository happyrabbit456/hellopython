a = "Hey"
print(len(a))

print(1+2)
print("1"+"2")

a = "pic123"
b = "21344"
print (a.isnumeric())
print (b.isnumeric())

e = "Once again he asked \"How long is a piece of string?\""
print(e)

msg = "ATTENTION!\rFor those about to rock, we salute you!"
print(msg)

msg = """This string
spans
multiple lines"""
print(msg)

msg = '''This string
spans
multiple lines'''
print(msg)

planet = "Jupiter"
print(planet[2])

planet = "Jupiter"
print(planet[2:5])

print("Hello %s, you scored %i out of %i" % ("Homer", 3, 100))

a = "Tea " + "Leaf"
print(a)

a = "Bee " * 3
print(a)
# Result
# Bee Bee Bee

a = "Mushroom"
print("m" in a)
print("b" in a)
print("shroo" in a)

a = "Mushroom"
print("m" not in a)
print("b" not in a)
print("shroo" not in a)

a = "1" + "\t" + "Bee"
b = "2" + r"\t" + "Tea"
print(a)
print(b)
# result
# 1		Bee
# 2\tTea

