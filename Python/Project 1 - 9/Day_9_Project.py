#Password Generator: Generates a random password of given length. Simple logic (just a random letter generator, not really a password), might recode

import random
password_bank = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                          "j", "k", "l", "m", "n", "o", "p", "q",
                            "r", "s", "t", "u", "v", "w", 'y',
                              'x', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]


def prompting():
    while True:
        prompt = int(input("Please enter the length of the password to generate: "))
        if 1 <= prompt <= 36:   
            break
        else:
            print("Please enter a number inbetween 1 and 35:")
        
    return prompt

def generator(length):
     while True:
        password = random.sample(password_bank,k=(length))
        "".join(password)
        return ("".join(password))
        break


def main():

    prompt = prompting()
    password_2 = generator(prompt)
    print("","\nYour password is:", password_2)
    

main()

