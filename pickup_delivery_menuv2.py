# Bugs
#Will only work for valid input "d" and "p"

# Menu so that the user can choose either pickup or delivery
#Invalid input triggers else statement but program does not ask for input again
print ("Do you want your order delivered or are you picking it up?")

print (" For delivery enter d")
print (" For Pickup enter p")

delivery = input()

if delivery == "d":
    print ("Delivery")

elif delivery == "p":
    print ("Pickup")

else:
    print ("That was not a valid input")
