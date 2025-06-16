#'Day_11_pt2_Project.py'


def calculator():
    while True:
        try:
            number1 = int(input("What is your first number?: "))
            break
        except ValueError:
            print("Please type a interger")
    operation = True        
    while operation == True:
        operation = input("What operation would you like to use? (A, S, M, D, SR) :")
        operation_list = {'A':0, 'S':1, 'M':2, 'D':3, 'SR':4}
        if operation in operation_list:
            number2 = int(input("What is your second number?: "))

            if operation == 'A':
                return (number1 + number2)
                break
            if operation == 'S':
                return (number1 - number2)
                break
            if operation == 'M':
                return (number1 * number2)
                break
            if operation == 'D':
                return (number1 / number2)
                break
            if operation == 'SR':
                return (number1 ** number2)
        else:
            print("Please enter a valid operation or interger")          
            return

def main():
    calculator()
    

if __name__== "__main__":
    main()
