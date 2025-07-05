#First ever python project! A simple prompt to learn conditionals

play = True
while play:
    length, width = float(input("What is the length?: ")), float(input("What is the girth?: "))
    if length > 6:
        print("Wow! Long!")
    elif 4 < length < 6:
        print("Cool medium")
    elif length < 4:
        print("A lil bit small")

    if width > 5:
        print("Wide moment")
    elif 3 < width < 5:
        print("Good medium!")
    elif width < 3:
        print("Bulk time!")

    noplay = input("Do you want keep playing, 'Y' or 'N': ")
    if noplay == "Y":
        play = True
    elif noplay == "N":
        play = False

    else: 
        print("Thats not 'Y' or 'N' :( ")
        play = False






