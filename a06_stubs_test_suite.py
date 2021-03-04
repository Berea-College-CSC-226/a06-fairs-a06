######################################################################
# Author: Silas Fair
# Username: fairs
#
# Assignment: A06: Stubs File Test Suite
# Purpose:  Test the rock paper get score function
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import sys

from a06_stubs import *


def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """
    # This function works correctly--it is verbatim from the text, Chapter 6

    linenum = sys._getframe(1).f_lineno                 # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def stubs_test_suite():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the functions in a06_stubs.

    :return: None
    """
    print("\nRunning the stubs test suite.")
    ##########################################
    print("\nTesting check_winner.")
    ##########################################

    testit(check_winner("rock", "rock") == "tie") # test a tie
    testit(check_winner("rock", "paper") == "loser")    # test a loss
    testit(check_winner("rock", "scissors") == "winner")    # test a win
    testit(check_winner("egg", "paper") == "egg")   # test the easter egg

    ##########################################
    print("\nEnding the a06_stubs_test_suite()).")


def main():
    """
    A 5 choice rock paper scissors game.

    :return: None
    """
    stubs_test_suite()


if __name__ == "__main__":
    main()
