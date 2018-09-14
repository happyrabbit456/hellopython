# Create the class
class MyClass:

    def __init__(self):
        self.a = "Hey"

    def b(self):
        return "Hello World"

    def MyFunc(self):
        return "Hello World"

# Object 1
o1 = MyClass()
print(o1.MyFunc())

# Create an object from the class
o = MyClass()

# Now we can work with the object
print(o.a)
print(o.b())

# Object 2
o2 = MyClass()
print(o2.MyFunc())


# Create the class
class Arithmetic:

    def Add(self, x, y):
        return x + y

    def Subtract(self, x, y):
        return x - y

    def Multiply(self, x, y):
        return x * y

    def Divide(self, x, y):
        return x / y


# Object 1
a = Arithmetic()
print(a.Add(2, 3))
print(a.Subtract(8, 300))
print(a.Multiply(2, 3))
print(a.Divide(30, 5))

# Object 2
b = Arithmetic()
print(b.Add(22, 33))
print(b.Subtract(88, 3333))
print(b.Multiply(77, 99))
print(b.Divide(555, 444))


# Create the class
class Person:

    def __init__(self, id, firstname, lastname, email):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def updateEmail(self, email):
        self.email = email

# Instantiate the class
user = Person(
    1,
    "Barney",
    "Rubble",
    ""
)

# Print details
print("First name:", user.firstname)
print("Last name:", user.lastname)
print("Email:", user.email)
print("===================")

# Add an email address
user.updateEmail("barney_rubble_123@example.com")

# Print details again
print("First name:", user.firstname)
print("Last name:", user.lastname)
print("Email:", user.email)


# Create the 'Person' class
class Person:

    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

# Create the 'Customer' class (inherited from the 'Person' class)
class Customer(Person):

    def __init__(self, id, firstname, lastname, totalspend):
        Person.__init__(self, id, firstname, lastname)
        self.totalspend = totalspend

    def getDetails(self):
        return "%s %s (customer %i) has spent %s in total." % (self.firstname, self.lastname, self.id, self.totalspend)

# Instantiate the 'Customer' class
customer = Customer(
    12,
    "Peter",
    "Griffin",
    13000
    )

# Print details
print(customer.getDetails())


a = "Hello World"

print(type(a))
print(a.__class__)


from src.calculations import multiplyMe

print(type(10))
print(type(1.0))
print(type([1,2,3]))
print(type((1,2,3)))
print(type({1,2,3}))
print(type({1:"Hello", 2:"World"}))
print(type(multiplyMe))
print(type(max))