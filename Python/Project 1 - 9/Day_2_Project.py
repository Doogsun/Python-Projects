#A converter for bodyweight

play = True
while play == True:
    wantplay = input("Weight converter. Type 'Yes' or 'No' to enter: ")
    if wantplay == "Yes":
            weight = float(input("Weight?: "))
            weightunit = input("What is the Unit (L or K?): ")
            if weightunit.upper() == "L":
                converted = weight / 2.2
                print("Weight in Kgs: " + str(converted)) 
            elif weightunit.upper() == "K":
                convertedk = weight * 2.2
                print("Weight in Lbs: " + str(convertedk))
            else: 
                print("Please Enter either 'L' or 'K' ")
                play = False
    elif wantplay.lower() == "no":
        print("Alrighty then buddy")
        play = False
    else:
        print("Please enter either Yes or No")
    





