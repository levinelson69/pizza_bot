# Pizza bot program
import random
from random import randint

#List of random names
names = ["Ross" , "Poppy" , "Joe" , "Sandy" , "Ben" , "Marisa" , "Steve" , "Susie" , "Jacob" , "Ziniac"]

num = randint(0,9)

name = (names[num])

print("*** Welcome to Dream Pizza ***")
print("*** My name is",name, "***")
print("I will be here to help you to order your delicious Dream Pizza")