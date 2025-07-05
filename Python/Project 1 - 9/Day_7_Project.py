#A converter for kms to miles and vice versa. First time def functions!



def KM_to_M (KM):
    convertedKM = KM*0.6213712
    return convertedKM

def M_to_KM (M):
    convertedM = M*1.609344
    return convertedM

play = True
while play:
    wantplay = input("Do you want to enter 'Y' or 'N': ").upper()
    if wantplay == "Y":
        distance_input = float(input("Enter a distance: "))
        distance_unit = input("What unit is that in? 'KM or 'Miles: ")
        if distance_unit == "KM":
            print(distance_input," KM", "converted to Miles is:", KM_to_M(distance_input))
            
        if distance_unit == "Miles":
            print(distance_input," Miles", "converted to KM is: ", M_to_KM(distance_input))
            
        
        else:
            print("Please enter either 'KM' or 'Miles'")

        
    if wantplay == "N":
        print("Okay bro")
        play = False

    else:
        print("Please enter 'Y' or 'N'")
        

