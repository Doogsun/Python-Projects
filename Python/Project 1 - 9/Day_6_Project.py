"""median.py
write a program that will take in a set of numbers untill the user enters a 0. It will then sort the list
 and print out a middle value, or median. If the list has an even number of elements, it was print out
   the average of the two middle values"""

list_1 = []

while True:
    set_1 = int(input("Enter a number to make a set. Enter '0' to stop: "))
    if set_1 == 0 :
        break        

    list_1.append(set_1)

list_length = len(list_1)
list_1.sort()

print(list_1)


if list_length % 2 == 1:
    print("Odd # of elements. Median of elements is:", list_1[list_length//2])
    
if list_length % 2 == 0:
    average = ((list_1[list_length//2 - 1]) + (list_1[(list_length//2)])) / 2
    print("Even # of elements. Average of 2 middle elements is:", average)

