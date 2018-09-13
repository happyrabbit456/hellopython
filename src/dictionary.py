# Create the dictionary
planet_size = {"Earth": 40075, "Saturn": 378675, "Jupiter": 439264}

# Print the dictionary
print(planet_size)

# Print the type
print(type(planet_size))

# Square brackets
print(planet_size["Earth"])

# get() function
print(planet_size.get("Saturn"))

# get() function without a default value
print(planet_size.get("Arrakis"))

# get() function with a default value
print(planet_size.get("Arrakis", "Huh?"))


# Create the dictionary
food = {"Fruit": ["Apple", "Orange", "Banana"], "Vegetables": ("Eat", "Your", "Greens")}

# Print the dictionary
print(food)


# Create the dictionary
food = {"Fruit": ["Apple", "Orange", "Banana"], "Vegetables": ("Eat", "Your", "Greens")}

# Print the second fruit item
print(food["Fruit"][1])


# Create the dictionary and print
user = {"Name": "Christine", "Age": 23}
print(user)

# Update the user's age and print
user["Age"] = 24
print(user)

# Add a new item and print
user["Height"] = 154
print(user)


# Create the dictionary and print
food = {"Fruit": ["Apple", "Orange", "Banana"]}
print(food)

# Update a list item and print
food["Fruit"][2] = "Watermelon"
print(food)


# Create dictionary and print
planet_size = {"Earth": 40075, "Saturn": 378675, "Jupiter": 439264}
print(planet_size)

# Delete an item then print
del planet_size["Jupiter"]
print(planet_size)

user = {"Name": "Christine", "Age": 23}
del user