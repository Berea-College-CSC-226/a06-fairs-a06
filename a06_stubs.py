#################################################################################
# Author(s): Silas Fair
# Username(s): fairs
#
# Assignment:a06 rock paper scissors.
# Purpose:Practice solving a problem more independently (without much / any starter code).
# More practice breaking a problem into pieces using functions.
# Even more practice with key concepts so far: loops, conditionals, and more!
##################################################################################
# Acknowledgements:
#
#
##################################################################################
import random

def check_winner(user, computer):
    """
    Check whether the user or computer wins.
    Print the result of the round, and add one life or take one away depending on.

    :param user: the choice the user entered. Rock, Paper, Scissors, Spock, Lizard.
    :param computer: the random computer selection. Rock, Paper, Scissors, Spock, Lizard.
    """
    winner = ""
    global lives
    global rounds
    if user == "scissors" and computer == "paper":
        return "winner"
    elif user == "paper" and computer == "spock":
        return "winner"
    elif user == "paper" and computer == "rock":
        return "winner"
    elif user == "lizard" and computer == "spock":
        return "winner"
    elif user == "spock" and computer == "scissors":
        return "winner"
    elif user == "scissors" and computer == "lizard":
        return "winner"
    elif user == "lizard" and computer == "paper":
        return "winner"
    elif user == "spock" and computer == "rock":
        return "winner"
    elif user == "rock" and computer == "scissors":
        return "winner"
    elif user == "egg":     # EASTER EGG
        return "egg"
    elif user == computer:  # if the user and computer choose the same thing declare a TIE!
        return "tie"
    else:   # if the computer wins. subtract 1 from lives, and check if player lost too many lives.
        return "loser"



def computer_choice():
    """
    computer chooses a random index
    return: computer choice
    """
    weapons = ["rock", "paper", "scissors", "lizard", "spock"]
    choice = random.choice(weapons)
    return choice


# Define and set global variables
global lives
lives = 10

global rounds
rounds = 0


def main():
    """
    Run the program
    """
    print("Choose one of the following: rock, paper, scissors, lizard, spock.")

    global lives
    global rounds
    # user input
    user_choice = ""
    possible_choices = ["rock", "paper", "scissors", "lizard", "spock","egg"]
    while user_choice not in possible_choices:  # ask for input until the user gives a valid input
        user_choice = input("Your choice: ").lower()
        if user_choice not in possible_choices:
            print("Not a valid choice. Try again.")

    # computer random choice
    computer = computer_choice()    # get the computer's choice
    print("Computer choice: " + computer)

    if check_winner(user_choice, computer) == "winner":     # win
        print(user_choice +" beats "+ computer)
        print("WINNER!")
        lives += 1
    elif check_winner(user_choice, computer) == "loser":    # loss
        lives -= 1
        print(user_choice + " loses to " + computer + ". \nYou LOST! ")
    elif check_winner(user_choice, computer) == "egg":  # EASTER EGG
        lives += 5
        print("You eat the egg. It gives you the strength to destroy " + computer + " with your bear hands. \nYou eating the egg, you have regained some health.")
    else:
        print("You both chose " + computer + ". \nIt's a TIE! ")    # tie

    # If the player's lives run out then show how many rounds they lasted.
    # and tell them they ran out of lives.
    if lives <= 0:
        print("You ran out of lives!")
        if rounds <= 20:
            print("You only lasted " + str(rounds) + " rounds!")
        else:
            print("You lasted " + str(rounds) + " rounds! Nice!")
        exit()
    elif lives >= 20:
        print("You made it to " + str(lives)+" lives!\nThe computer gives up.")
        exit()
    print("You have " + str(lives) + " lives remaining.\n")
    rounds += 1




while __name__ == "__main__":
    main()
