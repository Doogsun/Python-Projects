#Project that porvides feedback on your dick measurements lol :3

play = True
while play:
    dihlength, dihgirth = float(input("How long is your dih nga: ")), float(input("How girthy is your dih nga: "))
    if dihlength > 6:
        print("your shit kinda big bro")
    elif 4 < dihlength < 6:
        print("Your shit medium cuh")
    elif dihlength < 4:
        print("Your shit kinda small crodie")

    if dihgirth > 5:
        print("Your shit kinda thick")
    elif 3 < dihgirth < 5:
        print("Your shit girthy enough crodie")
    elif dihgirth < 3:
        print("Your shit skinny asf on foenem")

    noplay = input("Do you want keep playing, 'Y' or 'N': ")
    if noplay == "Y":
        play = True
    elif noplay == "N":
        play = False

    else: 
        print("Thats not 'Y' or 'N' cuh ")
        play = False






