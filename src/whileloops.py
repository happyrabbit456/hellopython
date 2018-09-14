counter = 1
while (counter < 10):
    print (counter)
    counter = counter +1

counter = 1
while (counter < 10):
    print (counter)
    counter = counter +1
    if counter == 5:
        break

counter = 1
while (counter < 10):
    print (counter)
    counter = counter +1
else:
    print("The loop has succesfully completed!")


# Note that the else doesn't execute if you break your loop:
counter = 1
while (counter < 10):
    print (counter)
    counter = counter +1
    if counter == 5:
        break
else:
    print("The loop has succesfully completed!")