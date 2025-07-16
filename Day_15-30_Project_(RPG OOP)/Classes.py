
import random
import time

class Warrior:

    def __init__(self, strstat, hpstat):

        self.strstat = strstat
        self.hpstat = hpstat
        self.isalive = True
        self.bleed = False
        self.concussed = False
    


    def basic_atk(self):
        print("\nA practiced swing of your sword cuts through the air.")
        damage = 2 + self.strstat
        return damage, 0


    def warriors_serrate(self):
        print("\nYou preform a swift dual slash-a cutting deep groves in your opponent")
        damage = 4 + self.strstat
        return damage, 1
        #bleeding = True


    def pommel_strike(self):
        print("\nYYou reverse your grip on the sword - CRACK! - hammering it with your heavy hilt!")
        damage = 6 + self.strstat
        return damage, 0
        #enemyhp -=3


    def whirlwind_spin(self):
        print("\nYou spin rapidly, sword extended in a wide cutting arc")
        damage = 8 + self.strstat
        return damage, 0 
        #enemyp -= 4


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
    


    def bleeding_apply(self, duration=2):
        self.bleed = True
        self.bleed_duration = duration
        time.sleep(2)
        print('\nYou start bleeding.')
        time.sleep(2)


    def processbleeding(self):

        if self.bleed == True:
            self.hpstat -= 1
            self.bleed_duration -= 1
            print(f"\nYou took 1 bleed damage ({self.bleed_duration} left)")
            time.sleep(2)

            if self.bleed_duration <= 0:
                self.bleed = False
                print("\nYou stop bleeding.")
                time.sleep(2)
        
            if self.hpstat <= 0:
                self.isalive = False


    def apply_concussed(self, duration=2):
        self.concussed = True
        self.missrate = 40
        self.concussed_duration = duration
        time.sleep(2)
        print(f"\nYou become concusssed")


    def process_concussed(self):
        missed = False
        if self.concussed == True:
            missmove = random.randint(1,100)
            
            if 1 <= missmove <= self.missrate:
                missed = True

            if missmove >= self.missrate + 1:
                missed = False

            print(f"\nYour are concussed.. {100 - self.missrate}% of move success")
            time.sleep(2)

            self.concussed_duration -= 1
            self.missrate - 20

            if self.concussed_duration <= 0:
                self.concussed = False
                print("\nYou are no longer concussed")

            if missed == False:
                return 0 
            if missed == True:
                return 1
            




class Wizard:

    def __init__(self, arcstat, hpstat):
        
        self.arcstat = arcstat
        self.hpstat = hpstat
        self.isalive = True
        self.bleed = False
        

    def basic_atk(self):
        print("\nYou send an arcane bolt at your opponent.")
        damage = 2 + self.arcstat
        return damage, 0
    

    def magic_rain(self):
        print("\nYou summon sharp, barbed-magical shards, that fall from above.")
        damage = 4 + self.arcstat
        return damage, 1
        #bleeding = True

    def magic_crackers(self):
        print("\nYou create explosive magical sparks that ignite on impact.")
        damage = 6 + self.arcstat
        return damage, 0 
        #enemyhp -= 3 


    def arcanus_pinnus(self):
        print("\nA large surge of magic converges into a small point- A thin beam pierces any foe.")
        damage = 8 + self.arcstat
        return damage, 0
        #enemyhp -= 4


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


    def bleeding_apply(self, duration=2):
        self.bleed = True
        self.bleed_duration = duration
        time.sleep(2)
        print('\nYou start bleeding.')
        time.sleep(2)


    def processbleeding(self):

        if self.bleed == True:
            self.hpstat -= 1
            self.bleed_duration -= 1
            print(f"\nYou took 1 bleed damage ({self.bleed_duration} left)")
            time.sleep(2)

            if self.bleed_duration <= 0:
                self.bleed = False
                print("\nYou stop bleeding.")
                time.sleep(2)
        
            if self.hpstat <= 0:
                self.isalive = False


class Rogue:

    def __init__(self, dexstat, hpstat):

        self.dexstat = dexstat
        self.hpstat = hpstat
        self.isalive = True
        self.bleed = False
        

    def basic_atk(self):
        print("\nAYou execute a smooth, in and out slice with your dagger.")
        damage = 2 + self.dexstat
        return damage, 0
     

    def ankle_cutter(self):
        print("\nA shadow slide across the floor-You slash at your opponents ankles.")
        damage = 4 + self.dexstat
        return damage, 1
        

    def dropkick_slash(self):
        print('\nA phaseflicker shrouds your movement.. You appear above your oppoenent, meteoring down and slasshing them.')
        damage = 6 + self.dexstat
        return damage, 0


    def thousand_flashstep(self):
        print("\nA flashstep slices through the air.. A flashtunnel of slashes sprials past your opponent.")
        damage = 8 + self.dexstat
        return damage, 0


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


    def bleeding_apply(self, duration=2):
        self.bleed = True
        self.bleed_duration = duration
        time.sleep(2)
        print('\nYou start bleeding.')
        time.sleep(2)


    def processbleeding(self):

        if self.bleed == True:
            self.hpstat -= 1
            self.bleed_duration -= 1
            print(f"\nYou took 1 bleed damage ({self.bleed_duration} left)")
            time.sleep(2)

            if self.bleed_duration <= 0:
                self.bleed = False
                print("\nYou stop bleeding.")
                time.sleep(2)
        
            if self.hpstat <= 0:
                self.isalive = False


#Could add a greater death scutscene and bar spacer but works for now
