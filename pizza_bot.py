# Pizza Bot Program
import random
from random import randint

#List of random 
names = ["Ross" , "Poppy" , "Joe" , "Sandy" , "Ben" , "Marisa" , "Steve" , "Susie" , "Jacob" , "Ziniac"]

# Welcome message with random name
def welcome():
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: none
    Returns: none
    '''
    
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Dream Pizza ***")
    print("*** My name is",name, "***")
    print("I will be here to help you to order your delicious Dream Pizza")


# Message for pickup or delivery






# Pick Up information - name and phone number






# Delivery information - name, address and phone





# Choose total number of Pizzas - max 5






# Pizza menu






# Pizza order - from menu - print each pizza ordered with cast





# Print order out - including if order is delivery or pickup and names and price of pizza - total cost including any delivery charge




# Ability to cancel or proceed with order





# Option for new order or to exit







# Main function
def main():
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: none
    Returns: none
    '''
    welcome()


main()

