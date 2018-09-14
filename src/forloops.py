planets = ["Earth", "Mars", "Neptune", "Venus", "Mercury", "Saturn", "Jupiter", "Uranus"]

for i in planets:
    print(i)

for i in planets:
    print(i)
else:
    print("That's all folks!")

for i in planets:
    print(i)
    if i == "Venus":
        break

# Note that the else doesn't execute if you break your loop:
for i in planets:
    print(i)
    if i == "Venus":
        break
else:
    print("That's all folks!")