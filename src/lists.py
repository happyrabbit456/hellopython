planets = ["Earth", "Mars", "Saturn", "Jupiter"]
print(len(planets))
print(planets[1])
print(planets[1:3])
print(planets[-2])

# Print the initial list
print(planets)

# Update the list item
planets[1] = "Mercury"

# Print the updated list
print(planets)

# Add the new list item
planets.append("Mercury")

# Print the updated list
print(planets)


# Delete the third list item
del planets[2]

# Print the updated list
print(planets)