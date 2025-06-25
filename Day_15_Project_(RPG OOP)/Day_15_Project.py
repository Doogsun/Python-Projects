"Practice oob and make a rpg with classes inspired by my third day project"

import time
import random


from Classes import Warrior, Wizard, Rogue




def Opening_menu():
    print("\nWelcome! This is the main menu. Choose a menu/option!\n\n  Fight ⚔️\n\n  Change Class 🧙\n\n  Exit ❌\n")
    menu_input = input("> ").upper()
    

    if menu_input in ("F", "FI", "FIG", "FIGH", "FIGHT", "⚔️"):
        print()

    elif menu_input in ("C", "CH", "CHA", "CHAN", "CHANG", "CHANGE", "CHANGE C", "CHANGE ", "CHANGE CL", "CHANGE CLA", "CHANGE CLAS", "CHANGE CLASS", "C", "CH", "CHA", "CHAN", "CHANG", 'CHANGE', '🧙'):
        print()

    elif menu_input in ("E", "EX", "EXI", "EXIT", "❌", 'BLEH'):
        print()
    


Opening_menu()


c