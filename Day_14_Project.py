"""Create a mental math trainer for double digit multiplication (XX * XX). Make modular to add more operations i nthe future"""


import random

operation_list = ["+", '-', '*']
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
again = False



def play_prompt():
    while again == True:
        play_again = str(input("Do you you want to play/play again? ('Y' or 'N'): " )).upper()
        if play_again == "Y":
            play = True
            return play
            
        if play_again == "N":
            play = False
            return play

        else:
            print("Please enter either 'Y' or 'N'")





def prompting():
    while True:
        try:
            question_amount = int(input("How many questions would you like to do? (1 - 50): "))
            operation_type = str(input("What operation would you like to do? (+, -, *): "))

            if 1 <= question_amount <= 50 and operation_type in operation_list:
                return question_amount, operation_type
            else:
                print("\nPlease enter a question amount between 1 - 50, and a valid operatino symbol.")

        except ValueError:
            print("\nThe first question requires a int, and the second question needs a str\n")





    
    


if __name__ == "__main__":
    again = True
    play1 = play_prompt()
    if play1 == True:
        prompting()
    
        

