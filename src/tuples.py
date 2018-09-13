# Set the tuples
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekenddays = "Saturday", "Sunday"

# Print the tuples
print(weekdays)
print(weekenddays)

# Print the second element of the tuple
print(weekdays[1])

print(weekdays[1:4])

a = ("dog")
b = ("dog",)
print(type(a))
print(type(b))

# Set the tuple
t = ("Banana", [1, 2, 3])

# Print the tuple
print(t)

t = (101, 202, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
print(t[2][1])

# Set two tuples
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekenddays = ("Saturday", "Sunday")

# Set a third tuple to the value of the previous two
alldays = weekdays + weekenddays

# Print them all
print(weekdays)
print(weekenddays)
print(alldays)


# Import the 'namedtuple' function from the 'collections' module
from collections import namedtuple

# Set the tuple
individual = namedtuple("Individual", "name age height")
user = individual(name="Homer", age=37, height=178)

# Print the tuple
print(user)

# Print each item in the tuple
print(user.name)
print(user.age)
print(user.height)