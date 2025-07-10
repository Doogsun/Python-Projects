
import random
import time

class Warrior:

    def __init__(self, strstat, hpstat):

        self.strstat = strstat
        self.hpstat = hpstat
        self.isalive = True
        
        

    def basic_atk(self):
        print("\nWith a hefty swing of ol-betsy.. you slash at your opponent.")
        #enemyhp -= 2 

    def warriors_serrate(self):
        print("\nol-betsy stances up.. a swift dual slash grates your opponent.")
        #enemyhp -= 2
        #bleeding = True


    def pommel_strike(self):
        print("\nYou swing your sword gracefully, weielding the pommel and hilt as a club.")
        #enemyhp -=3

    def whirlwind_spin(self):
        print("\nA vortex of wind empowers you.. You unleash a reckless flury of spining slashes.")


    def takedamage(self, damage): 
        self.hpstat -= damage
        time.sleep(2)
        print(f"\nYou took {damage} damage!\n")
        time.sleep(2)
        print(f"Your HP = {self.hpstat}\n")
        time.sleep(2)

        if self.hpstat <= 0:
            self.isalive = False
            wardeathmessage = random.randint(1,11)
            if wardeathmessage in (1, 2, 3, 4):
                print("You fell in battle.. You died.\n")
                time.sleep(2)

            if wardeathmessage in (5, 6, 7, 8, 9):
                print("You fall to your knees, helmet destroyed. You died\n")
                time.sleep(2)

            if wardeathmessage in (10, 11):
                print('Strong like a bull. Dead like a... dead guy?\n')
                time.sleep(2)
    
#Could add a greater death scutscene and bar spacer but works for now


class Wizard:

    def __init__(self, arcstat, hpstat):
        
        self.arcstat = arcstat
        self.hpstat = hpstat
        self.isalive = True
        

    def basic_atk(self):
        print("\nMagic pools around you.. You send an arcane bolt at your opponent.")
        #enemyhp -= 2 

    def magic_rain(self):
        print("\nMagic surges into the sky.. You rain spiked shards of arcane down onto your opponent.")
        #enemyhp -= 2
        #bleeding = True

    def magic_crackers(self):
        print("\nMagic explodes into life.. A show of magical sparklers set your enemey a blaze.")


    def arcanus_pinnus(self):
        print("\nA large surge of magic converges into a small point.. A thin beam donut anything in its path.")


    def takedamage(self, damage): 
        self.hpstat -= damage
        time.sleep(2)
        print(f"\nYou took {damage} damage!\n")
        time.sleep(2)
        print(f"Your HP = {self.hpstat}\n")
        time.sleep(2)

        if self.hpstat <= 0:
            self.isalive = False
            wizdeathmessage = random.randint(1,11)
            if wizdeathmessage in (1, 2, 3, 4,):
                print("You fell in battle.. You died.\n")
                time.sleep(2)

            if wizdeathmessage in (5, 6, 7, 8, 9):
                print("Magic leaves your body. You died\n")
                time.sleep(2)

            if wizdeathmessage in (10, 11):
                print('Maybe try using a HEAL spell next time. You died\n')
                time.sleep(2)

    

class Rogue:

    def __init__(self, dexstat, hpstat):

        self.dexstat = dexstat
        self.hpstat = hpstat
        self.isalive = True
        

    def basic_atk(self):
        print("\nA wisp of a robe is heard.. You execute a smooth, in and out slice with your dagger.")
        #enemyhp -= 2 

    def ankle_cutter(self):
        print("\nA shadow slids across the floor.. You slash at your opponents ankles.")
        #enemyhp -= 2
        #bleeding = True

    def dropkick_slash(self):
        print('\nA phaseflicker shrouds your movement.. You appear above your oppoenent, meteoring down and slasshing them.')


    def thousand_flashstep(self):
        print("\nA flashstep slices through the air.. A flashtunnel of slashes sprials past your flashstep.")


    def takedamage(self, damage): 
        self.hpstat -= damage
        time.sleep(2)
        print(f"\nYou took {damage} damage!\n")
        time.sleep(2)
        print(f"Your HP = {self.hpstat}\n")
        time.sleep(2)

        if self.hpstat <= 0:
            self.isalive = False
            rogdeathmessage = random.randint(1,11)
            if rogdeathmessage in (1, 2, 3, 4):
                print("You fell in battle.. You died.\n")
                time.sleep(2)

            if rogdeathmessage in (5, 6, 7, 8, 9):
                print("Your shrewd cloak turns a bright red. You died.\n")
                time.sleep(2)

            if rogdeathmessage in (10, 11):
                print('Stealth Stat = -99\n')
                time.sleep(2)



