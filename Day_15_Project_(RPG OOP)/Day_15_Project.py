"Practice oob and make a rpg with classes inspired by my third day project"

import time
import random


from Classes import Warrior, Wizard, Rogue

#1 = Fight, 2 = class change, 3 = exit
menu_index = [1 , 2, 3]





def Opening_menu():

    print("\nWelcome! This is the main menu.\n")

    while True:
        print("\nMain Menu --> Choose a menu/option!\n\n  Fight 💥\n\n  Change Class 📖\n\n  Exit ❌\n")
        menu_input = input("> ").upper()

        if menu_input in ("F", "FI", "FIG", "FIGH", "FIGHT", "⚔️"):
            return 1

        if menu_input in ("C", "CH", "CHA", "CHAN", "CHANG", "CHANGE", "CHANGE C", "CHANGE ", "CHANGE CL", "CHANGE CLA", "CHANGE CLAS", "CHANGE CLASS", "C", "CH", "CHA", "CHAN", "CHANG", 'CHANGE', '🧙'):
            return 2
            
        if menu_input in ("E", "EX", "EXI", "EXIT", "❌", 'BLEH'):
            break
              
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
            if stattype_war in ("S", 'ST', 'STA', 'STAN', 'STADA', 'STANDAR', 'STANDARD'):
                warstat1 = 2
                warstat2 = 2
                return (warstat1, warstat2)
                

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
            stattype_war = input("\n\nStat Menu --> Standard or Custom?\n\n> ").upper()
            if stattype_war in ("S", 'ST', 'STA', 'STAN', 'STADA', 'STANDAR', 'STANDARD'):
                wizstat1 = 2
                wizstat2 = 2
                return (wizstat1, wizstat2, set_class)
                

            elif stattype_war in ("C", 'CU', 'CUS', 'CUST', 'CUSTO', 'CUSTOM'):
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
            stattype_war = input("\n\nStat Menu --> Standard or Custom?\n\n> ").upper()
            if stattype_war in ("S", 'ST', 'STA', 'STAN', 'STADA', 'STANDAR', 'STANDARD'):
                rogstat1 = 2
                rogstat2 = 2
                return (rogstat1, rogstat2, set_class)
                

            elif stattype_war in ("C", 'CU', 'CUS', 'CUST', 'CUSTO', 'CUSTOM'):
                while True:
                    try:
                        print("\n--------------------------------------------")
                        rogstat1 = int(input("              Set the DEX stat.\n\n> "))
                        print("\n--------------------------------------------")
                        rogstat2 = int(input("              Set the HP stat.\n\n> "))
                        return (rogstat1, rogstat2, set_class)
                        
                        
                    except ValueError:
                        print("\nInvalid! Enter an integer")






def main():
    currentmenu = Opening_menu()
    if currentmenu in menu_index:
        if currentmenu == 1:
            ...
        elif currentmenu == 2:
            ChangeClass_Menu()


main()


