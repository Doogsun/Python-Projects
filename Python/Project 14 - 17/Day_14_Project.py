"""Create a mental math trainer for double digit multiplication (XX * XX). Make modular to add more operations i nthe future"""


import random
import time
import cowsay


def play_prompt():
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
    operation_list = ["+", '-', '*']

    while True:
        try:
            operation_type = str(input("What operation would you like to do? (+, -, *): "))
            operation_range = int(input("Select the terms range for the questions (1 - 100): "))
            question_amount = int(input("How many questions would you like to do? (1 - 50): "))

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
    addcorrect = 0
    addwrong = 0
    adddone = 0
    for question in range (1, question_amount + 1):
        try:
            addterm1 = random.randint(1, operation_range)
            addterm2 = random.randint(1, operation_range)
            addanswer = addterm1 + addterm2
            addinput = int(input(f"What is {addterm1} + {addterm2}?:  "))
            if addinput == addanswer:
                print("\nCorrect!\n")
                addcorrect += 1
                adddone += 1

            else:
                print("\nincorrect :(\n")
                addwrong += 1
                adddone += 1

        except ValueError:
            print("\nIncorrect! Please enter a interger\n")
            addwrong += 1
            adddone += 1

    if adddone == question_amount:
        addsmile = question_amount / 2
        if addcorrect > addsmile:
            print(f"You got {addcorrect}/{question_amount} Correct! You pass! :3\n  ")

        elif addcorrect < addsmile:
            print(f"You got {addcorrect}/{question_amount}. You failed :(\n ")
    

def subtraction(question_amount, operation_range):
    subcorrect = 0 
    subwrong = 0 
    subdone = 0
    for question in range(1, question_amount + 1):
        try:
            while True:
                subterm1 = random.randint(1, operation_range)
                subterm2 = random.randint(1, operation_range)
                if subterm1 >= subterm2:
                    subanswer = subterm1 - subterm2
                    subinput = int(input(f"What is {subterm1} - {subterm2} ?: "))
                    break
                

            if subinput == subanswer:
                print("\nCorrect!\n")
                subcorrect += 1
                subdone += 1

            else:
                print("\nincorrect :(\n")
                subwrong += 1
                subdone += 1


        except ValueError:
            print("\nIncorrect! Please enter a interger")
            subwrong += 1   
            subdone += 1

    if subinput == subanswer:
        addsmile = question_amount / 2
        if subcorrect > addsmile:
            print(f"You got {subcorrect}/{question_amount} Correct! You pass! :3\n  ")

        elif subcorrect < addsmile:
            print(f"You got {subcorrect}/{question_amount}. You failed :(\n ")


def multiplication(question_amount, operation_range):
    mulcorrect = 0
    mulwrong = 0
    muldone = 0
    for question in range (1, question_amount + 1):
        try:
            multerm1 = random.randint(1, operation_range)
            multerm2 = random.randint(1, operation_range)
            mulanswer = multerm1 * multerm2
            mulinput = int(input(f"What is {multerm1} x {multerm2} ?:  "))
            if mulinput == mulanswer:
                print("\nCorrect!\n")
                mulcorrect += 1
                muldone += 1

            else:
                print("\nincorrect :(\n")
                mulwrong += 1
                muldone += 1

        except ValueError:
            print("\nIncorrect! Please enter a interger\n")
            mulwrong += 1
            muldone += 1

    if muldone == question_amount:
        mulsmile = question_amount / 2
        if mulcorrect > mulsmile:
            print(f"You got {mulcorrect}/{question_amount} Correct! You pass! :3\n  ")

        elif mulcorrect < mulsmile:
            print(f"You got {mulcorrect}/{question_amount}. You failed :(\n ")


if __name__ == "__main__":
    play = play_prompt()
    while play == True:
       output1 = prompting()
       type_analysis(output1)
       play = play_prompt()
    

           
    


    
        



           
    


    
        

