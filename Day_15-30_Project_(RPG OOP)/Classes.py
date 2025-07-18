
import random
import time

class Warrior:

    def __init__(self, strstat, hpstat):

        self.strstat = strstat
        self.hpstat = hpstat
        self.isalive = True
        self.bleed = False
        self.concussed = False

        self.cooldowns = {"Warrior Serrate - 2": {"timer":2, "max": 2, "active": False},
                        "Pommel Strike - 3": {"timer":3, "max": 3, "active": False},
                        "Whirlwind Spin - 4": {"timer": 4, "max": 4, "active": False}}
        


    def update_cooldowns(self):

        for move, data in self.cooldowns.items():
            
            if data["active"]:
                data["timer"] -= 1
                if data["timer"] <= 0:
                    data["timer"] = data["max"]
                    data["active"] = False




    def move_select(self):

        self.update_cooldowns()

        while True:        


            


            print(f'\nMove Select Menu --> Entesr  | Name -> Use  |  Digit -> Info | \n\n  Basic Atk - 1 \n\n  Warrior Serrate - 2\n\n  Pommel Strike - 3\n\n  Whirlwind Spin - 4\n')
            prompt = input("> ")


            if prompt == '1': #basic atk info
                print('\n  "A simple slash of your sword."\n\n  Damage = 2 + strstat\n\n  Bleed = ❌\n\n  Cooldown = 1\n')
                time.sleep(2)

            if prompt == '2': #warrior serrate info
                print('\n  "A swift dual slash. Causes bleeding."\n\n  Damage = 4 + strstat\n\n  Bleed = ✅\n\n  Cooldown = 2')
                time.sleep(2)

            if prompt == '3': #pommel_strike info
                print('\n  "A blunt strike with your pommel"\n\n  Damage = 6 + strstat\n\n  Bleed = ❌\n\n  Cooldown = 3')
                time.sleep(2)

            if prompt == '4': #whirlwind strike info
                print('\n  "A spinning sword slash."\n\n  Damage = 8 + strstat\n\n  Bleed = ❌\n\n  Cooldown = 4')
                time.sleep(2)


            if prompt.upper() in ('B', 'BA', 'BAS', 'BASI', 'BASIC', 'BASIC ', 'BASIC A', 'BASIC AT', 'BASIC ATK'):
                attack = self.basic_atk()
                return attack
                

            if prompt.upper() in ('W', 'WA', 'WAR', 'WARR', 'WARRI', 'WARRIO', 'WARRIOR', 'WARRIOR ', 'WARRIOR S','WARRIOR SE', 'WARRIOR SERR', 'WARRIOR SERRA', 'WARRIOR SERRAT', 'WARRIOR SERRATE'):
                attack = self.warriors_serrate()
                self.cooldowns["Warrior Serrate - 2"]["active"] = True
                return attack


            if prompt.upper() in ('P', 'PO', 'POM', 'POMM', 'POMME', 'POMMEL', 'POMMEL ', 'POMMEL S', 'POMMEL ST', 'POMMEL STR', 'POMMEL STRI', 'POMMEL STRIK', 'POMMEL STRIKE'):
                attack = self.pommel_strike()
                self.cooldowns["Pommel Strike - 3"]["active"] = True
                return attack


            if prompt.upper() in ('WH', 'WHI', 'WHIR', 'WHIRL', 'WHIRLW', 'WHIRLWI', 'WHIRLWIND', 'WHIRLWIND ','WHIRLWIND S', 'WHIRLWIND SP', 'WHIRLWIND SPI', 'WHIRLWIND SPIN'):
                attack = self.whirlwind_spin()
                self.cooldowns["Whirlwind Spin - 4"]["active"] = True
                return attack


            else:
                print("\nPlease Enter | Name -> Use  |  Digit -> Info ")



            
            


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
        


    def move_select(self):
        while True:
            print('\nMove Select Menu --> Enter  | Name -> Use  |  Digit -> Info | \n\n  Basic Atk - 1\n\n  Magic Rain - 2\n\n  Magic Crackers - 3\n\n  Arcanus Pinnus - 4\n')
            prompt = input("> ")

            if prompt == '1': 
                print('\n  "A bolt of arcane."\n\n  Damage = 2 + arcstat\n\n  Bleed = ❌\n\n  Cooldown = 1')

            elif prompt == '2': 
                print('\n  "A hail of sharp magic rain. Causes bleeding."\n\n  Damage = 4 + arcstat\n\n  Bleed = ✅\n\n  Cooldown = 2')

            elif prompt == '3': 
                print('\n  "Arcane sparks that explode on contact. (Make sure to enter crackers not magic)."\n\n  Damage = 6 + arcstat\n\n  Bleed = ❌\n\n  Cooldown = 3')

            elif prompt == '4': 
                print('\n  "A concetrated magic beam."\n\n  Damage = 8 + arcstat\n\n  Bleed = ❌\n\n  Cooldown = 4')



            if prompt.upper() in ('B', 'BA', 'BAS', 'BASI', 'BASIC', 'BASIC ', 'BASIC A', 'BASIC AT', 'BASIC ATK'):
                damage =self.basic_atk()
                return damage

            elif prompt.upper() in ('M', 'MA', 'MAG', 'MAGI', 'MAGIC', 'MAGIC ', 'MAGIC R', 'MAGIC RA', 'MAGIC RAI', 'MAGIC RAIN'):
                self.magic_rain()
                return damage

            elif prompt.upper() in ('C', 'CR,', 'CRA', 'CRAC', 'CRACK', 'CRACKE', 'CRACKER', 'CRACKERS', 'MAGIC C', 'MAGIC CR', 'MAGIC CRA', 'MAGIC CRAC', 'MAGIC CRACK', 'MAGIC CRACKE', 'MAGIC CRACKER', 'MAGIC CRACKERS'):
                self.magic_crackers()
                return damage

            elif prompt.upper() in ('A', 'AR', 'ARC', 'ARCA', 'ARCAN', 'ARCANU', 'ARCANUS','ARCANUS ', 'ARCANUS P', 'ARCANUS PI', 'ARCANUS PIN', 'ARCANUS PINN', 'ARCANUS PINNU', 'ARCANUS PINNUS'):
                self.arcanus_pinnus()
                return damage

            else:
                print("\nPlease Enter | Name -> Use  |  Digit -> Info ")




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
        

    def move_select(self):
        while True:
            print('\nMove Select Menu --> Enter  | Name -> Use  |  Digit -> Info | \n\n  Basic Atk - 1\n\n  Ankle Cutter - 2\n\n  Dropkick Slash - 3\n\n  Thousand Flashstep - 4\n')
            prompt = input("> ").upper()

            if prompt == 1: 
                print('\n  "A slice of your dagger."\n\n  Damage = 2 + arcstat\n\n  Bleed = ❌\n\n  Cooldown = 1')

            elif prompt == 2: 
                print('\n  "A hail of sharp magic rain. Causes bleeding."\n\n  Damage = 4 + arcstat\n\n  Bleed = ✅\n\n  Cooldown = 2')

            elif prompt == 3: 
                print('\n  "Arcane sparks that explode on contact."\n\n  Damage = 6 + arcstat\n\n  Bleed = ❌\n\n  Cooldown = 3')

            elif prompt == 4: 
                print('\n  "A concetrated magic beam."\n\n  Damage = 8 + arcstat\n\n  Bleed = ❌\n\n  Cooldown = 4')


            if prompt in ('B', 'BA', 'BAS', 'BASI', 'BASIC', 'BASIC ', 'BASIC A', 'BASIC AT', 'BASIC ATK'):
                self.basic_atk()


            elif prompt in ('A', 'AN', 'ANK', 'ANKL', 'ANKLE', 'ANKLE ', 'ANKLE C', 'ANKLE CU', 'ANKLE CUT', 'ANKLE CUTT', 'ANKLE CUTTE', 'ANKLE CUTTER'):
                self.ankle_cutter()


            elif prompt in ('D', 'DR', 'DRO', 'DROP', 'DROPK', 'DROPKI', 'DROPKIC', 'DROPKICK', 'DROPKICK ','DROPKICK S', 'DROPKICK SL', 'DROPKICK SLA', 'DROPKICK SLAS', 'DROPKICK SLASH'):
                self.dropkick_slash()


            elif prompt in ('T', 'TH', 'THO', 'THOU', 'THOUS', 'THOUSA', 'THOUSAN', 'THOUSAND', 'THOUSAND ','THOUSAND F', 'THOUSAND FL', 'THOUSAND FLA', 'THOUSAND FLAS', 'THOUSAND FLASH','THOUSAND FLASHS', 'THOUSAND FLASHST', 'THOUSAND FLASHSTE', 'THOUSAND FLASHSTEP'):
                self.thousand_flashstep()


            else:
                print("\nPlease Enter | Name -> Use  |  Digit -> Info ")
    

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




warrior = Warrior(1,1)
while True:
    warrior.move_select()
#Could add a greater death scutscene and bar spacer but works for now
