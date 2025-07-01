"Practice oob and make a rpg with classes inspired by my third day project"

import time
import random


from Classes import Warrior, Wizard, Rogue
from Enemies import Goblin, Golem, RAH


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
                warstat1 = ...
                warstat2 = ...
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
                wizstat1 = ...
                wizstat2 = ...
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
                rogstat1 = ...
                rogstat2 = ...
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
            while True:
                stattype_goblin = input("\n\nStat Menu --> Standard or Random or Custom?\n*Warning. Random stat will not be balanced..*\n\n> ").upper()
                if stattype_goblin in ('S', 'ST', 'STA', 'STAN', 'STAND', 'STANDA', 'STANDAR', 'STANDARD'):
                    goblinstat1 = ...
                    goblinstat2 = ...
                if stattype_goblin in ('R', 'RA', 'RAN', 'RAND', 'RANDO', 'RANDOM'):
                    
                    goblinstat1 = random.randint(1, 10)
                    goblinstat2 = random.randint(1, 10)
                
                if stattype_goblin in ('C', 'CU', 'CUS', 'CUST', 'CUSTO', 'CUSTOM'):
                    while True:
                            try:
                                print("\n--------------------------------------------")
                                goblinstat1 = int(input("              Set the Level.\n\n> "))
                                print("\n--------------------------------------------")
                                goblinstat2 = int(input("              Set the BaseHP stat.\n\n> "))
                                return ...
                                
                                
                            except ValueError:
                                print("\nInvalid! Enter an integer")


                print(f"\nYour Class: {select_class}")
                print("Your opponent: Goblin\n")
                print(f"The Goblin stats: BaseHp Stat = {goblinstat2}, Level = {goblinstat1},")

                print("\nEnter Confirm or Deny\n")
                goahead = input("> ")
                if goahead in ('C', 'CO', 'CON', 'CONF', 'CONFI', 'CONFIR', 'CONFIRM'):
                    break
                if goahead in ('D', 'DE', 'DEN', 'DENY'):
                    pass



        if fight_input in ('S', 'ST', 'STO', 'STON', 'STONE', 'G', 'G', 'GO', 'GOL', 'GOLE', 'GOLEM', 'GOLEM ', 'STONE ' 'STONE', 'STONE G', 'STONE GO', 'STONE GOL', 'STONE GOLE', 'STONE GOLEM'):
            while True:
                stattype_stone = input("\n\nStat Menu --> Standard or Random or Custom?\n*Warning. Random stat will not be balanced..*\n\n> ").upper()
                if stattype_stone in ('S', 'ST', 'STA', 'STAN', 'STAND', 'STANDA', 'STANDAR', 'STANDARD'):
                    stonestat1 = ...
                    stonestat2 = ...
                if stattype_stone in ('R', 'RA', 'RAN', 'RAND', 'RANDO', 'RANDOM'):
                    
                    stonestat1 = random.randint(1, 10)
                    stonestat2 = random.randint(1, 10)
                
                if stattype_stone in ('C', 'CU', 'CUS', 'CUST', 'CUSTO', 'CUSTOM'):
                    while True:
                            try:
                                print("\n--------------------------------------------")
                                stonestat1 = int(input("              Set the Level.\n\n> "))
                                print("\n--------------------------------------------")
                                stonestat2 = int(input("              Set the BaseHP stat.\n\n> "))
                                return ...
                                
                                
                            except ValueError:
                                print("\nInvalid! Enter an integer")


                print(f"\nYour Class: {select_class}")
                print("Your opponent: Stone Golem\n")
                print(f"The Stone Golem's stats: BaseHp Stat = {stonestat2}, Level = {stonestat1},")

                print("\nEnter Confirm or Deny\n")
                goahead = input("> ")
                if goahead in ('C', 'CO', 'CON', 'CONF', 'CONFI', 'CONFIR', 'CONFIRM'):
                    break
                if goahead in ('D', 'DE', 'DEN', 'DENY'):
                    pass

        


        if fight_input in ('R', 'RA', 'RAH','RAH ','RAH T', 'RAH TH', 'RAH THE', 'RAH THE ', 'RAH THE S', 'RAH THE SU', 'RAH THE SUN', 'bleh', 'RAH THE SUN ', 'RAH THE SUN G', 'RAH THE SUN GO', 'RAH THE SUN GOD', '☀️'):
            while True:
                stattype_RAH = input("\n\nStat Menu --> Standard or Random or Custom?\n*Warning. Random stat will not be balanced..*\n\n> ").upper()
                if stattype_RAH in ('S', 'ST', 'STA', 'STAN', 'STAND', 'STANDA', 'STANDAR', 'STANDARD'):
                    RAHstat1 = ...
                    RAHstat2 = ...
                if stattype_RAH in ('R', 'RA', 'RAN', 'RAND', 'RANDO', 'RANDOM'):
                    
                    RAHstat1 = random.randint(1, 10)
                    RAHstat2 = random.randint(1, 10)
                
                if stattype_RAH in ('C', 'CU', 'CUS', 'CUST', 'CUSTO', 'CUSTOM'):
                    while True:
                            try:
                                print("\n--------------------------------------------")
                                RAHstat1 = int(input("              Set the Level.\n\n> "))
                                print("\n--------------------------------------------")
                                RAHstat2 = int(input("              Set the BaseHP stat.\n\n> "))
                                return ...
                                
                                
                            except ValueError:
                                print("\nInvalid! Enter an integer")


                print(f"\nYour Class: {select_class}")
                print("Your opponent: RAH THE SUN GOD ☀️\n")
                print(f"RAH THE SUN GODS stats: BaseHp Stat = {RAHstat2}, Level = {RAHstat1},")

                print("\nEnter Confirm or Deny\n")
                goahead = input("> ")
                if goahead in ('C', 'CO', 'CON', 'CONF', 'CONFI', 'CONFIR', 'CONFIRM'):
                    break
                if goahead in ('D', 'DE', 'DEN', 'DENY'):
                    pass





def fighting():
    pass




def main():
    
    runamount = 1 #checks to display the welcome message

    while True:
        currentmenu = Opening_menu(runamount)
        if currentmenu in menu_index:
            if currentmenu == 1:
                try:
                    runamount += 2
                    fight_menu(changeoutput)

                except UnboundLocalError:
                    print("\n\nPlease select a class first. (Change class)")


            elif currentmenu == 2:
                changeoutput = ChangeClass_Menu()
                runamount += 1
               
            elif currentmenu == 3:
                break
            

        


main()


