# Rock-paper-scissors-lizard-Spock

# Importing the required modules

import math
import random

# This function maps a string to a numeric value

def name_to_number(name):
    # The following ifs/elifs compare the string passed
    # in name to the following cases and return a value for rpsls to use.
    # function return -1 if an improper name is presented
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Invalid selection:", name
        return -1

# This function maps a numeric value to a string

def number_to_name(number):
    # The following ifs/elifs compare the value passed
    # in number to the following cases and return the appropriate name rpsls to use.
    # function return -1 if an improper name is presented
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Invalid selection:", number
        return -1
    

def rpsls(player_choice): 
    """
    This is where the magic happens.
    This function is passed the players choice and then selects
    a random choice for the computer.  Interger values are assigned
    to the choices to facilitate comparision. After subtracting the
    players choice from the computers choice, modulo 5 is performed
    on the result. This leaves us with single digit value to determine
    the winner.  0 is a tie. 1-2 means the player won. 3-4 means the
    won.
    """
        
    # print a blank line to separate consecutive games
    print "\n"
    
    # print out the message for the player's choice
    print "Player chooses", (player_choice)
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number =  name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number =  random.randrange(0,5,1)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", (comp_choice)
    
    # Compute difference of comp_number and player_number then modulo five
    a = (player_number - comp_number)%5

    # Usin if/elif/else to determine winner, the print winner message
    if a == 0:
        print "It's a tie!"
        
    elif a <= 2:
        print "Player wins!"
       # print "If the remainder is 3 then the decision may be wrong.  Check your math."
        
    else:
        print "Computer wins!"
    
# The function is called five times, once for each possible value for testing
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




