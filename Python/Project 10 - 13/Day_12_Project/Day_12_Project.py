"""File io stuff!!
r = read (default)
w = write, truncate
r+ = read/write
w+ = read/write, truncate
a+ = read/append
a = append

"""

#for line in cleaned_balance:
    #print(f"A previous input was {line}")


while True:
    try:
        remaining_balance = int(input("How much money do you have left?: "))
        with open("Money.txt", 'a') as file:
            file.write(f"{remaining_balance}\n")
            break
    except ValueError:
        print("Please enter a valid interger")


with open("Money.txt", 'r') as file: #reads the list
    balance = file.readlines()


cleaned_balance = [line.strip() for line in balance] #strips the \n from the balance list for use


interger_list = [int(number.replace("'", '')) for number in cleaned_balance] #logically sound version to preform calculations

    #creates a list and for each line (number) replaces 

