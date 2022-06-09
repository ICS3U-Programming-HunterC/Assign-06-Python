#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: June 2, 2022
# This program asks the user to enter a sentence. The program will then call a
# function that accepts the user's sentence as a string and converts it to an
# int where it then calculates the integers by the multiplier. Then it will
# return the values where it displays the multiplied numbers on the same lines
# the program will then ask if the user wants to play again


def string_parcer(integers, multiplier):
    # split the sentence into multiple words
    list_of_int = integers.split(", ")

    # convert the list to integers
    list_of_int = list(map(float, list_of_int))

    # multiply the numbers by the multiplier
    multiplied_list = [a_num * multiplier for a_num in list_of_int]
    
    my_formatted_list = [ '%.2f' % a_num for a_num in multiplied_list ]

    # return the list of multiplied numbers
    return my_formatted_list


def main():

    # declare the list
    list_of_int = []

    # greet the user
    print(
        "This program accepts a list of numbers and a multiplier and then it will "
        "return a new list where each of the first numbers are multiplied!!"
    )

    # ask the user if they want to play
    play_again = input("Would you like to play? (y/n): ")

    while play_again == "yes" or play_again == "y":

        # get the user input
        integers = input("Enter a list of integers seperated by commas(,): ")
        try:
            # get the multiplier
            multiplier = float(input("Enter a multiplier: "))
            # call the function
            list_of_int = string_parcer(integers, multiplier)

            # display the output to the user
            print("The product of each element with the multiplier is:", end=" ")
            for a_num in list_of_int:
                print(a_num, end=", ")
            print()

            # ask the user if they want to play again
            play_again = input("Do you want to play again?: ")
            print("")

            # if they enter yes it will continue, if they enter anything
            # else, the program will end
            if play_again == "yes" or play_again == "y":
                continue
            else:
                print("Thanks for playing!!")
                break
        except:
            print("Invalid input!, please enter a valid list of numbers!")


if __name__ == "__main__":
    main()
