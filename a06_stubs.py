#################################################################################
# Author(s): Silas Fair
# Username(s): fairs
#
# Assignment:a06 rock paper scissors.
# Purpose:Practice solving a problem more independently (without much / any starter code).
# More practice breaking a problem into pieces using functions.
# Even more practice with key concepts so far: loops, conditionals, and more!
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import random

def check_winner(user, computer):
    """
    Check whether the user or computer wins. Print the result of the round, and add 1 to the winner's score.

    :param user: the choice the user entered. Rock, Paper, Scissors, Spock, Lizard.
    :param computer: the random computer selection. Rock, Paper, Scissors, Spock, Lizard.
    """
    winner = ""
    global lives
    if user == "scissors" and computer == "paper":
        print("Scissors cut paper.")
        print("WINNER!")
        lives += 1
    elif user == "paper" and computer == "spock":
        print("Paper disproves Spock.")
        print("WINNER!")
        lives += 1
    elif user == "paper" and computer == "rock":
        print("Paper covers Rock")
        print("WINNER!")
        lives += 1
    elif user == "lizard" and computer == "spock":
        print("Lizard poisons Spock.")
        print("WINNER!")
        lives += 1
    elif user == "spock" and computer == "scissors":
        print("Spock smashes scissors.")
        print("WINNER!")
        lives += 1
    elif user == "scissors" and computer == "lizard":
        print("Scissors decapitate lizard.")
        print("WINNER!")
        lives += 1
    elif user == "lizard" and computer == "paper":
        print("Lizard eats paper.")
        print("WINNER!")
        lives += 1
    elif user == "spock" and computer == "rock":
        print("Spock vaporizes rock.")
        print("WINNER!")
        score += 1
    elif user == "rock" and computer == "scissors":
        print("Rock crushes scissors.")
        print("WINNER!")
        lives += 1
    elif user == computer:
        print("You both chose " + computer+ ". \nIt's a TIE! ")
    else:
        lives -= 1
        print(user+ " is beaten by " + computer+ ". \nYou LOST! ")
        if lives <= 0:
            print("You ran out of lives!")
            exit()
    print("You have " +str(lives)+" lives remaining.")



def computer_choice():
    """
    computer chooses a random index
    return: computer choice
    """
    weapons = ["rock", "paper", "scissors", "lizard", "spock"]
    choice = random.choice(weapons)
    return choice

global lives
lives = 10

def main():
    """
    Run the program
    """
    print("Choose one of the following: rock, paper, scissors, lizard, spock.")

    user_choice = ""
    while user_choice not in ["rock", "paper", "scissors", "lizard", "spock"]:
        user_choice = input("Your choice: ")
    computer = computer_choice()
    print("Computer choice:")
    check_winner(user_choice, computer)




while __name__ == "__main__":
    main()
