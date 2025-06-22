"""Create a mental math trainer for double digit multiplication (XX * XX). Make modular to add more operations i nthe future"""


import random
import time

operation_list = ["+", '-', '*']
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
            operation_range = int(input("Select the terms range for the questions (1 - 100): "))


            if 1 <= question_amount <= 50 and (operation_type in operation_list) and 1 <= operation_range <= 100:
                return question_amount, operation_type, operation_range
            else:
                print("\nPlease enter a question amount between 1 - 50, and a valid operatino symbol.")

        except ValueError:
            print("\nThe first question requires a int, and the second question needs a str\n")


def type_analysis(tupleoutput):
    if tupleoutput[1] == "+":
        addition(tupleoutput[0], tupleoutput[2])
        return None
    
    elif tupleoutput[1] == "-":
        subtraction(tupleoutput[0], tupleoutput[2])
        return None
    
    elif tupleoutput[1] == "*":
        multiplication(tupleoutput[0], tupleoutput[2])
        return None


def addition(question_amount, operation_range):
    correct = 0
    wrong = 0
    for question in range (1, question_amount + 1):
        try:
            term1 = random.randint(1, operation_range)
            term2 = random.randint(1, operation_range)
            answer = int(input(f"{term1} + {term2}: "))
            
        except ValueError:
            print("Please enter a correct answer format (int)")
           
 


def subtraction(question_amount, operation_range):
    print()

def multiplication(question_amount, operation_range):
    print()



if __name__ == "__main__":
    again = True
    play1 = play_prompt()
    if play1 == True:
       output1 = prompting()
       type_analysis(output1)

           
    


    
        

