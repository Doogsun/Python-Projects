"Practice oob and make a rpg with classes inspired by my third day project"

import time
import random
import sys

from Classes import Warrior, Wizard, Rogue
from Enemies import Goblin, Golem, RAH
from Goblin_art import goblin_art1, goblin_art2
from Golem_art import golem_art1
from RAH_art import Rah_art1, Rah_art2


#1 = Fight, 2 = class change, 3 = exit
menu_index = [1 , 2, 3]



def Opening_menu(runamount):


    if runamount == 1:
        print("\nWELCOME ADVENTURER! We need your help! There are 3, vicous monsters we need you to slay...\nChoose your class and defaet these foes! --> This is the main menu\n ")

    elif runamount > 1:
        ...

    while True:
        print("\nMain Menu --> Choose a menu/option!\n\n  Fight 💥\n\n  Change Class 📖\n\n  Exit ❌\n")
        menu_input = input("> ").upper()

        if menu_input in ("F", "FI", "FIG", "FIGH", "FIGHT", "⚔️"):
            runamount += 1 
            return 1

        if menu_input in ("C", "CH", "CHA", "CHAN", "CHANG", "CHANGE", "CHANGE C", "CHANGE ", "CHANGE CL", "CHANGE CLA", "CHANGE CLAS", "CHANGE CLASS", "C", "CH", "CHA", "CHAN", "CHANG", 'CHANGE', '🧙'):
            runamount += 1
            return 2
            
        if menu_input in ("E", "EX", "EXI", "EXIT", "❌", 'BLEH'):
            runamount += 1
            return 3
              
        else:
            None



def ChangeClass_Menu():

    print("\n\n Charcter Selection --> Select a class")
    while True:
        print("\n  Warror ⚔️\n\n  Wizard 🧙\n\n  Rogue 🌫️\n")
        class_input = input("> " ).upper()

        if class_input in ("W", 'WA', 'WAR', 'WARR', 'WARRI', 'WARRIO', 'WARRIOR'):
            set_class = "WAR"
            stattype_war = input("\n\nStat Menu --> Standard or Custom?\n\n> ").upper()
            if stattype_war in ("S", 'ST', 'STA', 'STAN', 'STAND', 'STANDA' 'STANDAR', 'STANDARD'):
                warstat1 = 10
                warstat2 = 20
                return (warstat1, warstat2, set_class)
                

            elif stattype_war in ("C", 'CU', 'CUS', 'CUST', 'CUSTO', 'CUSTOM'):
                while True:
                    try:
                        print("\n--------------------------------------------")
                        warstat1 = int(input("              Set the STR stat.\n\n> "))
                        print("\n--------------------------------------------")
                        warstat2 = int(input("              Set the HP stat.\n\n> "))
                        return (warstat1, warstat2, set_class)
                        
                        
                    except ValueError:
                        print("\nInvalid! Enter an integer")




        if class_input in ("W", 'WI', 'WIZ', 'WIZA', 'WIZAR', 'WIZARD'):
            set_class = "WIZ"
            stattype_wiz = input("\n\nStat Menu --> Standard or Custom?\n\n> ").upper()
            if stattype_wiz in ("S", 'ST', 'STA', 'STAN', 'STAND', 'STANDA' 'STANDAR', 'STANDARD'):
                wizstat1 = 10
                wizstat2 = 20
                return (wizstat1, wizstat2, set_class)
                

            elif stattype_wiz in ("C", 'CU', 'CUS', 'CUST', 'CUSTO', 'CUSTOM'):
                while True:
                    try:
                        print("\n--------------------------------------------")
                        wizstat1 = int(input("              Set the ARC stat.\n\n> "))
                        print("\n--------------------------------------------")
                        wizstat2 = int(input("              Set the HP stat.\n\n> "))
                        return (wizstat1, wizstat2, set_class)
                        
                        
                    except ValueError:
                        print("\nInvalid! Enter an integer")



        if class_input in ('R', 'RO', 'ROG', 'ROGU', 'ROGUE'):
            set_class = "ROG"
            stattype_rog = input("\n\nStat Menu --> Standard or Custom?\n\n> ").upper()
            if stattype_rog in ("S", 'ST', 'STA', 'STAN', 'STAND', 'STANDA' 'STANDAR', 'STANDARD'):
                rogstat1 = 10
                rogstat2 = 20
                return (rogstat1, rogstat2, set_class)
                

            elif stattype_rog in ("C", 'CU', 'CUS', 'CUST', 'CUSTO', 'CUSTOM'):
                while True:
                    try:
                        print("\n--------------------------------------------")
                        rogstat1 = int(input("              Set the DEX stat.\n\n> "))
                        print("\n--------------------------------------------")
                        rogstat2 = int(input("              Set the HP stat.\n\n> "))
                        return (rogstat1, rogstat2, set_class)
                        
                        
                    except ValueError:
                        print("\nInvalid! Enter an integer")



def fight_menu(changeoutput): #ADD A feature to where you can set stas (level) of enemy or make it random, have it return stat data for enemies/ selected enemy
    if changeoutput[2] == "WAR":
        select_class = "Warrior"

    elif changeoutput[2] == "WIZ":
        select_class = "Wizard"

    elif changeoutput[2] == "ROG":
        select_class = 'Rogue'

    while True:
        print("\n\nFight Menu --> Choose a opponent!\n\n  Goblin 🪓\n\n  Stone Golem 🪨\n\n  RAH THE SUN GOD ☀️\n")
        fight_input = input("> ").upper()
        
        if fight_input in ('G', 'GO', 'GOB', 'GOBL', 'GOBLI', 'GOBLIN'):
            enemy = "GOB"
            while True:
                stattype_goblin = input("\n\nStat Menu --> Standard or Random or Custom?\n*Warning. Random stat will not be balanced..*\n\n> ").upper()
                if stattype_goblin in ('S', 'ST', 'STA', 'STAN', 'STAND', 'STANDA', 'STANDAR', 'STANDARD'):
                    goblinstat1 = 5
                    goblinstat2 = 10
                if stattype_goblin in ('R', 'RA', 'RAN', 'RAND', 'RANDO', 'RANDOM'):
                    
                    goblinstat1 = random.randint(1, 20)
                    goblinstat2 = random.randint(1, 20)
                
                if stattype_goblin in ('C', 'CU', 'CUS', 'CUST', 'CUSTO', 'CUSTOM'):
                    while True:
                            try:
                                print("\n--------------------------------------------")
                                goblinstat1 = int(input("              Set the Level.\n\n> "))
                                print("\n--------------------------------------------")
                                goblinstat2 = int(input("              Set the BaseHP stat.\n\n> "))
                                break
                                
                                
                            except ValueError:
                                print("\nInvalid! Enter an integer")


                print(f"\nYour Class: {select_class}")
                print("Your opponent: Goblin\n")
                print(f"The Goblin stats: BaseHp Stat = {goblinstat2}, Level = {goblinstat1},")

                print("\nEnter Confirm or Deny\n")
                goahead = input("> ").upper()
                if goahead in ('C', 'CO', 'CON', 'CONF', 'CONFI', 'CONFIR', 'CONFIRM'):
                    
                    return (goblinstat1, goblinstat2, enemy)

                if goahead in ('D', 'DE', 'DEN', 'DENY'):
                    pass



        if fight_input in ('S', 'ST', 'STO', 'STON', 'STONE', 'G', 'G', 'GO', 'GOL', 'GOLE', 'GOLEM', 'GOLEM ', 'STONE ' 'STONE', 'STONE G', 'STONE GO', 'STONE GOL', 'STONE GOLE', 'STONE GOLEM'):
            enemy = "STONE"
            while True:
                stattype_stone = input("\n\nStat Menu --> Standard or Random or Custom?\n*Warning. Random stat will not be balanced..*\n\n> ").upper()
                if stattype_stone in ('S', 'ST', 'STA', 'STAN', 'STAND', 'STANDA', 'STANDAR', 'STANDARD'):
                    stonestat1 = 10
                    stonestat2 = 20
                if stattype_stone in ('R', 'RA', 'RAN', 'RAND', 'RANDO', 'RANDOM'):
                    
                    stonestat1 = random.randint(1, 30)
                    stonestat2 = random.randint(1, 30)
                
                if stattype_stone in ('C', 'CU', 'CUS', 'CUST', 'CUSTO', 'CUSTOM'):
                    while True:
                            try:
                                print("\n--------------------------------------------")
                                stonestat1 = int(input("              Set the Level.\n\n> "))
                                print("\n--------------------------------------------")
                                stonestat2 = int(input("              Set the BaseHP stat.\n\n> "))
                                break
                                
                                
                            except ValueError:
                                print("\nInvalid! Enter an integer")


                print(f"\nYour Class: {select_class}")
                print("Your opponent: Stone Golem\n")
                print(f"The Stone Golem's stats: BaseHp Stat = {stonestat2}, Level = {stonestat1},")

                print("\nEnter Confirm or Deny\n")
                goahead = input("> ").upper()
                if goahead in ('C', 'CO', 'CON', 'CONF', 'CONFI', 'CONFIR', 'CONFIRM'):
                    
                    return (stonestat1, stonestat2, enemy)

                if goahead in ('D', 'DE', 'DEN', 'DENY'):
                    pass

        


        if fight_input in ('R', 'RA', 'RAH','RAH ','RAH T', 'RAH TH', 'RAH THE', 'RAH THE ', 'RAH THE S', 'RAH THE SU', 'RAH THE SUN', 'bleh', 'RAH THE SUN ', 'RAH THE SUN G', 'RAH THE SUN GO', 'RAH THE SUN GOD', '☀️'):
            enemy = "RAH"
            while True:
                stattype_RAH = input("\n\nStat Menu --> Standard or Random or Custom?\n*Warning. Random stat will not be balanced..*\n\n> ").upper()
                if stattype_RAH in ('S', 'ST', 'STA', 'STAN', 'STAND', 'STANDA', 'STANDAR', 'STANDARD'):
                    RAHstat1 = 15
                    RAHstat2 = 30
                if stattype_RAH in ('R', 'RA', 'RAN', 'RAND', 'RANDO', 'RANDOM'):
                    
                    RAHstat1 = random.randint(1, 30)
                    RAHstat2 = random.randint(1, 30)
                
                if stattype_RAH in ('C', 'CU', 'CUS', 'CUST', 'CUSTO', 'CUSTOM'):
                    while True:
                            try:
                                print("\n--------------------------------------------")
                                RAHstat1 = int(input("              Set the Level.\n\n> "))
                                print("\n--------------------------------------------")
                                RAHstat2 = int(input("              Set the BaseHP stat.\n\n> "))
                                break
                                
                                
                            except ValueError:
                                print("\nInvalid! Enter an integer")


                print(f"\nYour Class: {select_class}")
                print("Your opponent: RAH THE SUN GOD ☀️\n")
                print(f"RAH THE SUN GODS stats: BaseHp Stat = {RAHstat2}, Level = {RAHstat1},")

                print("\nEnter Confirm or Deny\n")
                goahead = input("> ").upper()
                if goahead in ('C', 'CO', 'CON', 'CONF', 'CONFI', 'CONFIR', 'CONFIRM'):
                    
                    return (RAHstat1, RAHstat2, enemy)

                if goahead in ('D', 'DE', 'DEN', 'DENY'):
                    pass



def fighting(fightdata, changeoutput): #fightdata ---> (enemystat1, hpstat, 'enemyfought':GOB,STONE,RAH)

    player_class = changeoutput[2]
    if player_class == "WAR":
        player1 = Warrior(changeoutput[0], changeoutput[1])

    elif player_class == "WIZ":
        player1 = Wizard(changeoutput[0], changeoutput[1])

    elif player_class == "ROG":
        player1 = Rogue(changeoutput[0], changeoutput[1])




    if fightdata[2] == "GOB":
        goblin1 = Goblin(fightdata[0], fightdata[1])
        

        #gob_cutscene1()       #temp takewawy for QOL         #changeoutput ---> (10, 20, 'CLASS':WAR,ROG,WIZ)
        
        
        print('\n"A GOBLIN!!"\n')

        time.sleep(2)

        dead = False #If player or enemy dies, then dead is turned to true
        flee = False #if player sucessfully flees then flee is turned to true
        fleelocked = False #check to see aleady fleed for a turn
        
        

        if player_class == "WAR":

                coollist = {1:"Basic Atk", 2:"Serrate", 3:"Pommel Strike", 4:"Whirlwind Spin"}
                ablelist = ["Basic Atk", "Serrate", "Pommel Strike", "Whirlwind Spin"]

                funclist = {
                    1: player1.basic_atk,
                    2: player1.warriors_serrate,
                    3: player1.pommel_strike,
                    4: player1.whirlwind_spin
                }

        if player_class == "WIZ":

                coollist = {1:"Basic Atk", 2:"Magic Rain", 3:"Magic Crackers", 4:"Arcanus Pinnus"}
                ablelist = ["Basic Atk", "Magic Rain", "Magic Crackers", "Arcanus Pinnus"]

                funclist = {
                    1: player1.basic_atk,
                    2: player1.magic_rain,
                    3: player1.magic_crackers,
                    4: player1.arcanus_pinnus
                }

        if player_class == "ROG":
            coollist = {1:"Basic Atk", 2:"Ankle Cutter", 3:"Dropkick Slash", 4:'"Thousand" Flashstep'}
            ablelist = ["Basic Atk", "Ankle Cutter", "Dropkick Slash", '"Thousand" Flashstep']

            funclist = {
                1: player1.basic_atk,
                2: player1.ankle_cutter,
                3: player1.dropkick_slash,
                4: player1.thousand_flashstep
                }
           
        
        
        while dead or flee == False:

            if player1.isalive == False:
                dead += True
                break

            if goblin1.isalive == False:
                dead += True
                break

            # 1. Loop through the coolist
            # 2. Subtract 1 from all the cooldown values
            # 3. If cooldown value of skill is 0 or lower remove skill from cooldown list 
            
            if goblin1.evovled == False:
                print(goblin_art1) 

            if goblin1.evovled == True:
                print(goblin_art2)

            print("\n  Move\n\n  Flee\n")
            turninput = input("> ").upper()

            if turninput in ('M', 'MO', 'MOV', 'MOVE'):
                funclist[1]()
                goblin1.takedamage(3)

                move = goblin1.choose_move()
                player1.takedamage(move)
                fleelocked = False
        
                                

                            
                               
                       








    
                       

                        
                       
                        
                            

                        





                    
    

















            elif turninput in ('F', 'FL', 'FLE', 'FLEE'):


                if fleelocked == True:
                    print("\nYou cannot attempt a to flee again this turn.")
                    time.sleep(2)
                    
                    
                if fleelocked == False:
                    fleeattempt = random.randint(1,3) #placeholder for random.ranint
                    checkattempt = 1 #always suceeds escape

                    fleemessage = "Atemptting to flee"
                    for i in range(4):
                        dots = "." * i 
                        sys.stdout.write(f"\r{fleemessage}{dots}  ")
                    
                        sys.stdout.flush()
                        time.sleep(1.5)


                    if fleeattempt == checkattempt:

                        print("You suceeded! :3")
                        time.sleep(2)
                        flee = True
                        
                    
                    if fleeattempt != checkattempt :

                        print("You Failed! :(")
                        time.sleep(2)
                        flee = False
                        fleelocked = True

            else:
                print('\nPlease enter a valid input')
                time.sleep(2)


    if fightdata[2] == "STONE":
        stone1 = Golem(fightdata[0], fightdata[1])



        stone_cutscene1()       #temp takewawy for QOL         #changeoutput ---> (10, 20, 'CLASS':WAR,ROG,WIZ)
        
        
        print('\nA COLOSSAL golem emerges!\n')

        time.sleep(2)

        dead = False #If player or enemy dies, then dead is turned to true
        flee = False #if player sucessfully flees then flee is turned to true
        fleelocked = False #check to see aleady fleed for a turn
        
        

        if player_class == "WAR":

                coollist = {1:"Basic Atk", 2:"Serrate", 3:"Pommel Strike", 4:"Whirlwind Spin"}
                ablelist = ["Basic Atk", "Serrate", "Pommel Strike", "Whirlwind Spin"]

                funclist = {
                    1: player1.basic_atk,
                    2: player1.warriors_serrate,
                    3: player1.pommel_strike,
                    4: player1.whirlwind_spin
                }

        if player_class == "WIZ":

                coollist = {1:"Basic Atk", 2:"Magic Rain", 3:"Magic Crackers", 4:"Arcanus Pinnus"}
                ablelist = ["Basic Atk", "Magic Rain", "Magic Crackers", "Arcanus Pinnus"]

                funclist = {
                    1: player1.basic_atk,
                    2: player1.magic_rain,
                    3: player1.magic_crackers,
                    4: player1.arcanus_pinnus
                }

        if player_class == "ROG":
            coollist = {1:"Basic Atk", 2:"Ankle Cutter", 3:"Dropkick Slash", 4:'"Thousand" Flashstep'}
            ablelist = ["Basic Atk", "Ankle Cutter", "Dropkick Slash", '"Thousand" Flashstep']

            funclist = {
                1: player1.basic_atk,
                2: player1.ankle_cutter,
                3: player1.dropkick_slash,
                4: player1.thousand_flashstep
                }
           

        
        
        while dead or flee == False:

            if player1.isalive == False:
                dead += True
                break

            if stone1.isalive == False:
                dead += True
                break

            # 1. Loop through the coolist
            # 2. Subtract 1 from all the cooldown values
            # 3. If cooldown value of skill is 0 or lower remove skill from cooldown list 
            
            print(golem_art1)

            print("\n  Move\n\n  Flee\n")
            turninput = input("> ").upper()

            if turninput in ('M', 'MO', 'MOV', 'MOVE'):
                fleelocked = False
        
                                

                            
                               
                       








    
                       

                        
                       
                        
                            

                        





                    
    

















            elif turninput in ('F', 'FL', 'FLE', 'FLEE'):


                if fleelocked == True:
                    print("\nYou cannot attempt a to flee again this turn.")
                    time.sleep(2)
                    
                    
                if fleelocked == False:
                    fleeattempt = random.randint(1,3) #placeholder for random.ranint
                    checkattempt = 1 #always suceeds escape

                    fleemessage = "Atemptting to flee"
                    for i in range(4):
                        dots = "." * i 
                        sys.stdout.write(f"\r{fleemessage}{dots}  ")
                    
                        sys.stdout.flush()
                        time.sleep(1.5)


                    if fleeattempt == checkattempt:

                        print("You suceeded! :3")
                        time.sleep(2)
                        flee = True
                        
                    
                    if fleeattempt != checkattempt :

                        print("You Failed! :(")
                        time.sleep(2)
                        flee = False
                        fleelocked = True

            else:
                print('\nPlease enter a valid input')
                time.sleep(2)


    if fightdata[2] == "RAH":
        rah1 = RAH(fightdata[0], fightdata[1])

        rah_cutscene1()

        time.sleep(2)
        print("")

        print("\nI AM RAH, THE GOD OF THE SUN! FACE MY DIVINE FORM!!")

        time.sleep(2)

        dead = False #If player or enemy dies, then dead is turned to true
        flee = False #if player sucessfully flees then flee is turned to true
        fleelocked = False #check to see aleady fleed for a turn
        
        

        if player_class == "WAR":

                coollist = {1:"Basic Atk", 2:"Serrate", 3:"Pommel Strike", 4:"Whirlwind Spin"}
                ablelist = ["Basic Atk", "Serrate", "Pommel Strike", "Whirlwind Spin"]

                funclist = {
                    1: player1.basic_atk,
                    2: player1.warriors_serrate,
                    3: player1.pommel_strike,
                    4: player1.whirlwind_spin
                }

        if player_class == "WIZ":

                coollist = {1:"Basic Atk", 2:"Magic Rain", 3:"Magic Crackers", 4:"Arcanus Pinnus"}
                ablelist = ["Basic Atk", "Magic Rain", "Magic Crackers", "Arcanus Pinnus"]

                funclist = {
                    1: player1.basic_atk,
                    2: player1.magic_rain,
                    3: player1.magic_crackers,
                    4: player1.arcanus_pinnus
                }

        if player_class == "ROG":
            coollist = {1:"Basic Atk", 2:"Ankle Cutter", 3:"Dropkick Slash", 4:'"Thousand" Flashstep'}
            ablelist = ["Basic Atk", "Ankle Cutter", "Dropkick Slash", '"Thousand" Flashstep']

            funclist = {
                1: player1.basic_atk,
                2: player1.ankle_cutter,
                3: player1.dropkick_slash,
                4: player1.thousand_flashstep
                }
        
        

        while dead or flee == False:


            # 1. Loop through the coolist
            # 2. Subtract 1 from all the cooldown values
            # 3. If cooldown value of skill is 0 or lower remove skill from cooldown list 
            
            if rah1.trueform == True:
                print(Rah_art2)

            if rah1.trueform == False:
                print(Rah_art1)


            print("\n  Move\n\n  Flee\n")
            turninput = input("> ").upper()

            if turninput in ('M', 'MO', 'MOV', 'MOVE'):
                
                funclist[3]()
                rah1.takedamage(10)
                if rah1.isalive == False:
                    dead += True
                    break

                damage = rah1.choose_move()
                player1.takedamage(damage)
                if player1.isalive == False:
                    dead += True
                    break

                fleelocked = False
        
                                

                            
                               
                       








    
                       

                        
                       
                        
                            

                        





                    
    

















            elif turninput in ('F', 'FL', 'FLE', 'FLEE'):


                if fleelocked == True:
                    print("\nYou cannot attempt a to flee again this turn.")
                    time.sleep(2)
                    
                    
                if fleelocked == False:
                    fleeattempt = random.randint(1,3) #placeholder for random.ranint
                    checkattempt = 1 #always suceeds escape

                    fleemessage = "Atemptting to flee"
                    for i in range(4):
                        dots = "." * i 
                        sys.stdout.write(f"\r{fleemessage}{dots}  ")
                    
                        sys.stdout.flush()
                        time.sleep(1.5)


                    if fleeattempt == checkattempt:

                        print("You suceeded! :3")
                        time.sleep(2)
                        flee = True
                        
                    
                    if fleeattempt != checkattempt :

                        print("You Failed! :(")
                        time.sleep(2)
                        flee = False
                        fleelocked = True

            else:
                print('\nPlease enter a valid input')
                time.sleep(2)









def gob_cutscene1():

    time.sleep(0.6)
    print()
    time.sleep(0.6)
    print()
    time.sleep(0.6)                 
    print()
    time.sleep(0.6)
    print()
    time.sleep(0.6)

    print("-------------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(0.75)

    print("\nThere is an unease in the air.")

    for i in range(3):
        time.sleep(1)
        print('...')
        time.sleep(1)

    print("\nA cool breeze chills your spine.")

    for i in range(3):
        time.sleep(1)
        print("...")
        time.sleep(1)

    time.sleep(1)


def stone_cutscene1():
    
    time.sleep(0.6)
    print()
    time.sleep(0.6)
    print()
    time.sleep(0.6)                 
    print()
    time.sleep(0.6)
    print()
    time.sleep(0.6)

    print("-------------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(0.75)

    print('\nThe ground starts shaking..')

    for i in range(2):
        time.sleep(0.7)
        print('THUMP\n')
        time.sleep(0.7)

    for i in range(3):
        time.sleep(0.25)
        print('THUMP\n')
        time.sleep(0.25)


    time.sleep(1)


def rah_cutscene1():
    time.sleep(0.6)
    print()
    time.sleep(0.6)
    print()
    time.sleep(0.6)                 
    print()
    time.sleep(0.6)
    print()
    time.sleep(0.6)

    print("-------------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(2.75)
    
    print('\n"A voice radiates from above"')
    time.sleep(4)
    
    print("\nWhat do we have here?\n")
    time.sleep(4)
    message = "Hmm"
    for i in range(4):
        dots = "." * i 
        sys.stdout.write(f"\r{message}{dots}   ")
        
        sys.stdout.flush()
        time.sleep(1)

    print("")
    time.sleep(1.5)
        
    print("\nI see. You've come to slay me!\n")
    time.sleep(1.5)
    

    message2 = "HA"
    for i in range(5):
        laugh = "HA" * i 
        sys.stdout.write(f"\r{message2}{laugh}   ")
        
        sys.stdout.flush()
        time.sleep(0.5)

    time.sleep(1)

    message3 = "Truly Pitiful"
    for i in range(4):
        dots2 = "." * i 
        sys.stdout.write(f"\r{message3}{dots2}   ")
        
        sys.stdout.flush()
        time.sleep(1)

    



def main():
    
    runamount = 1 #checks to display the welcome message

    while True:
        currentmenu = Opening_menu(runamount)
        if currentmenu in menu_index:
            if currentmenu == 1:
                #try:
                    runamount += 2
                    fightdata = fight_menu(changeoutput)
                    fighting(fightdata, changeoutput)

                #except 
                    #print("\n\nPlease select a class first. (Change class)")

#checks for to see if class is seleceted or not, temp takeway for debugging

            elif currentmenu == 2:
                changeoutput = ChangeClass_Menu()
                runamount += 1
               
            elif currentmenu == 3:
                break
            

   

if __name__ == "__main__":
    main()


