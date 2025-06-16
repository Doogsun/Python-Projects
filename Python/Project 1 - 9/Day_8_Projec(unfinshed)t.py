"""Prime Checker: Returns True if a number is prime. Recoded """

import sys

def prompting():
    try:
        output = int(input("Please enter a number: "))
        output
    except ValueError and TypeError:
        print("Please enter in a NUMBER DUDE!")



def prime_checker(num):
    if num < 2:
        return "Number is not prime"
    elif num == 2:
        return "Number is prime"
    elif num > 2 and num % 2 == 1:
        if num % 3 > 1:
            return False
        elif num % 4 > 1:
            return False
        elif num % 5 > 1:
            return False
            



def main():
    check = prompting()
    print(prime_checker(check))


if __name__ == "__main__":
    main()



#prime numbers
#1. their odd (except 2) --- check if the number is 2 or 1, then check if their is a remainder when divided by 2 
#2. no other divisors other than themselves and 1
#3. natural numberrs (no decimals) 
