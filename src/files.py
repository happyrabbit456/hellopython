# Create the file in 'write' mode
f = open("hello.txt", "w")

# Write some text to the file
f.write("Hello World!")

# Close the file
f.close()


# Open the file in 'read' mode
f = open("hello.txt", "r")

# Put the contents of the file into a variable
f_contents = f.read()

# Close the file
f.close()

# Print the file's contents
print(f_contents)


# Read the original file and print
f = open("hello.txt", "r")
f_contents = f.read()
print("Original content:", f_contents)
f.close()

# Update the file
f = open("hello.txt", "w")
f_contents = "Hey there Jupiter!"
f.write(f_contents)
f.close()

# Read the updated file and print
f = open("hello.txt", "r")
f_contents = f.read()
print("Updated content:", f_contents)
f.close()


# Read the original file and print
f = open("hello.txt", "r")
f_contents = f.read()
print("Original content:", f_contents)
f.close()

# Update the file
f = open("hello.txt", "a")
f_contents = "\r\n" + "Hey there Uranus!"
f.write(f_contents)
f.close()

# Read the updated file and print
f = open("hello.txt", "r")
f_contents = f.read()
print("Updated content:", f_contents)
f.close()

# Read a Single Line
f = open("hello.txt", "r")
line1 = f.readline()
line2 = f.readline()
print("Line 1:", line1)
print("Line 2:", line2)
f.close()

# Looping over the Lines
f = open("hello.txt", "r")
for line in f:
    print("Line:", line, end="")
f.close()


# Read Multiple Lines as a List
# Using 'readlines()'
f = open("hello.txt", "r")
f_content = f.readlines()
print(f_content)
f.close()

# Using 'list()'
f = open("hello.txt", "r")
f_content = list(f)
print(f_content)
f.close()