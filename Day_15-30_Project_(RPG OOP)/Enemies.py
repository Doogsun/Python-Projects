import random
import time
import sys



class Goblin: 

    def __init__ (self, level, hpstat):

        self.level = level
        self.dscale = 0
        self.bleed = False

        
        if self.level >= 10:
            self.dscale = 2
        if self.level >= 20:
            self.dscale = 3
        if self.level >= 30:
            self.dscale = 4

        self.hpstat = hpstat + (2 * level)
        if hpstat > 0:
            self.isalive = True

        self.evovled = False

        



    def choose_move(self):
        missed = False
        goblinmove = random.randint(1,100)
        gobmessage = "The goblin is deciding"
        for i in range(4):
            dots = "." * i 
            sys.stdout.write(f"\r{gobmessage}{dots}   ")
        
            sys.stdout.flush()
            time.sleep(1)


        if 1 <= goblinmove <= 53:
            used = "Punch"

        if 54 <= goblinmove <= 76:
            used = "Smash"
    
        if 77 <= goblinmove < 97:
            used = "Fury Swipes"

        if goblinmove in (97, 98, 99, 100):
            used = "Evolve"

        print("")
        time.sleep(1)
        print(f'\nThe goblin decides to use "{used}"\n')
        time.sleep(2)

        goblinmiss = random.randint(1,100)
       
        if 1<= goblinmiss <= 20:
            missed = True

        if 21<= goblinmiss <= 100:
            missed = False
            
        if missed == True:
            time.sleep(1)
            print(f'The goblin misses "{used}"\n')
            time.sleep(2)
            return 0, 0, 0


        if missed == False:            #1:damage, 2:bleeding, 3:concussed
            if 1 <= goblinmove <= 53:
                self.punch()
                dealt = 1 + self.dscale
                return dealt, 0, 0

            if 54 <= goblinmove <= 76:
                self.smash()
                dealt = 2 + self.dscale
                return dealt, 0, 0
        
            if 77 <= goblinmove < 97:
                self.fury()
                dealt = 3 + self.dscale
                return dealt, 1, 0
                #bleeding

            if goblinmove in (97, 98, 99, 100):
                self.evolve()
                return 0, 0, 0
                



    def punch(self):
        print("\nThe goblin snarls and throws a wild, dirt-caked fist straight at your gut.")
        

    def smash(self):
        print("\nWith a screech, the goblin leaps—smashing both fists down like a falling rock")
        #hp -= 2 
        

    def fury(self):
        print('\nEyes blazing, it goes feral-a flurry of wild kicks and slashes slashes your legs')
        #hp -=3
        #bleeding = True


    def evolve(self):

        print("\nGRAVITY HAS BROUGHT ME HERE FOR A REASON...\nTHE STARS HAVE ALIGNED.\nTHE TIME OF EVOLUTION IS NOW!!!")
        time.sleep(5)
        self.hpstat += 20
        self.evovled = True

        #become cmoon and kill everyone


    def takedamage(self, damage):
        self.hpstat -= damage
        time.sleep(2)
        print(f"\nThe goblin took {damage} damage.\n")
        time.sleep(2)
        print(f"The goblin's HP = {self.hpstat}\n")
        time.sleep(2)

        if self.hpstat <= 0:
            self.isalive = False

        if self.isalive == False:
            print("The goblin died\n") #placeholder for death cutscene or smth
            time.sleep(2)
        

    def bleeding_apply(self, duration=2):
        self.bleed = True
        self.bleed_duration = duration
        time.sleep(2)
        print('\nThe goblin starts bleeding.')
        time.sleep(2)


    def processbleeding(self):

        if self.bleed == True:
            self.hpstat -= 2 
            self.bleed_duration -= 1

            if self.bleed_duration > 0:
                print(f"\nThe goblin took 2 bleed damage ({self.bleed_duration} left)")
                time.sleep(2)

            if self.bleed_duration <= 0:
                print(f"\nThe goblin took 2 bleed damage ({self.bleed_duration} left)\n")
                time.sleep(2)
                self.hpstat -= 2
                self.bleed = False
                print("\nThe goblin stops bleeding.")
                time.sleep(2)
        
            if self.hpstat <= 0:
                self.isalive = False
         

class Golem:

    def __init__(self, level, hpstat):
        self.level = level
        self.dscale = 0
        self.bleed = False

        if self.level >= 10:
            self.dscale = 2
        if self.level >= 20:
            self.dscale = 3
        if self.level >= 30:
            self.dscale = 4

        self.hpstat = hpstat + (2 * level)
        if hpstat > 0:
            self.isalive = True


    def choose_move(self):
        missed = False
        golemmove = 70 #random.randint(1,100)       for concussed testing
        golmessage = "The golem is deciding"
        for i in range(4):
            dots = "." * i 
            sys.stdout.write(f"\r{golmessage}{dots}   ")
        
            sys.stdout.flush()
            time.sleep(1)


        if 1 <= golemmove <= 43:
            used = "Strong Left"

        if 44 <= golemmove <= 66:
            used = "Breaker Combo"
    
        if 67 <= golemmove <= 87:
            used = "Thunder Clap"

        if  88 <= golemmove <= 100:
            used = "Grug"

        print("")
        time.sleep(1)
        print(f'\nThe Golem uses "{used}"\n')
        time.sleep(2)

        
        stonemiss = random.randint(1,100)
        
        if 1 <= stonemiss <= 15:
            missed = True

        if 16 <= stonemiss <= 100:
            missed = False
            
        if missed == True:
            time.sleep(1)
            print(f'The golem misses "{used}"\n')
            time.sleep(2)
            return 0, 0, 0


        if 1 <= golemmove <= 43:
            self.strongleft()
            dealt =  1 + self.dscale
            return dealt, 0, 0

        if 44 <= golemmove <= 66:
            self.breakercombo()
            dealt = 2 + self.dscale
            return dealt, 0, 0
    
        if 67 <= golemmove <= 87:
            self.thunderclap()
            dealt = 2 + self.dscale
            return dealt, 0, 1
            #concussed
            

        if  88 <= golemmove <= 100:
            self.grug()
            return 0, 0, 0



    def strongleft(self):
        print("\nThe golem's left arm grinds forward—a crushing boulder fist slams down!")
        #hp -= 2
    
    def breakercombo(self):
        print("\nStone fists blur in a flurry—RIGHT, LEFT, RIGHT—each hit shakes the ground.")
        #hp -= 4 

    def thunderclap(self):
        print("\nThe golem smashes its fists together—a shockwave booms, concussing you.")
        #hp -= 3 
        #concussed

    def grug(self):
        print("\nThe golem rumbles deeply... 'Grug.' Crumbling rocks reform, healing its wounds.")
        self.hpstat += 7


    def takedamage(self, damage):
        self.hpstat -= damage
        time.sleep(2)
        print(f"\nThe Golem took {damage} damage.\n")
        time.sleep(2)
        print(f"The Golem's HP = {self.hpstat}\n")
        time.sleep(2)

        if self.hpstat <= 0:
            self.isalive = False

        if self.isalive == False:
            print("The golem died\n") #placeholder for death cutscene or smth
            time.sleep(2)

        
    def bleeding_apply(self, duration=2):
            self.bleed = True
            self.bleed_duration = duration
            time.sleep(2)
            print('\nThe golem starts bleeding.')
            time.sleep(2)


    def processbleeding(self):

        if self.bleed == True:
            self.hpstat -= 2 
            self.bleed_duration -= 1
            print(f"\nThe golem took 2 bleed damage ({self.bleed_duration} left)")
            time.sleep(2)

            if self.bleed_duration <= 0:
                print(f"\nThe golem took 2 bleed damage ({self.bleed_duration} left)")
                time.sleep(2)
                self.hpstat -= 2
                self.bleed = False
                print("\nThe golem stops bleeding.")
                time.sleep(2)
        
            if self.hpstat <= 0:
                self.isalive = False
    

class RAH:

    def __init__(self, level, hpstat):
        self.level = level
        self.dscale = 0
        self.bleed = False

        if self.level >= 10:
            self.dscale = 2
        if self.level >= 20:
            self.dscale = 3
        if self.level >= 30:
            self.dscale = 4

        self.hpstat = hpstat + (2 * level)
        if hpstat > 0:
            self.isalive = True

        self.trueform = False



    def choose_move(self):
        missed = False
        rahmove = random.randint(1,100)
        rahmessage = 'The Prescence of a god is felt'
        for i in range(4):
            dots = "." * i 
            sys.stdout.write(f"\r{rahmessage}{dots}   ")
        
            sys.stdout.flush()
            time.sleep(1)

        if rahmove == 1:
            used = "TRUEFORM"

        if 2 <= rahmove <= 43:
            used = "Ray of Sun"

        if 44 <= rahmove <= 66:
            used = "Solar Shards"
    
        if 67 <= rahmove <= 87:
            used = "Bolts of RAH"

        if  88 <= rahmove <= 100:
            used = "RAHWRATH"

    
        print("")
        time.sleep(1)
        print(f'\nRAHs will is set. "{used}!"\n')
        time.sleep(2)


        rahmiss = random.randint(1,100)
        
        if 1<= rahmiss <= 15:
            missed = True

        if 16<= rahmiss <= 100:
            missed = False
            

        if missed == True:
            time.sleep(1)
            print(f'RAH misses "{used}"\n')
            time.sleep(2)
            return 0, 0, 0

        if rahmove == 1:
            self.trueformed()
            return 0, 0, 0

        if 2 <= rahmove <= 43:
            self.Ray_Of_Sun()
            dealt = 2 + self.dscale
            return dealt, 0, 0

        if 44 <= rahmove <= 66:
            self.Solar_shards()
            dealt = 4 + self.dscale
            return dealt, 1, 0
    
        if 67 <= rahmove <= 87:
            self.Bolts_of_RAH()
            dealt = 3 + self.dscale
            return dealt, 0, 1
            
        if  88 <= rahmove <= 100:
            self.RAHWARTH()
            dealt = 10 + self.dscale
            return dealt, 0, 0



    def Ray_Of_Sun(self):
        print('"A blazing beam of divine light scorches down—"OBEY THE LIGHT!"')
        #hpstat -= 3

    def Bolts_of_RAH(self):
        print("The sky darkens as searing pillars of judgment strike from above.")
        #hpstat -= 4
        #concussed = True

    def Solar_shards(self):
        print('Shards of a shattered star rain down, burning and cutting with cruelty.')
        #hpstat -= 3
        #bleeding = True

    def RAHWARTH(self):
        print('The suns full fury erupts—"THIS ENDS NOW!"')
        #hpstat -= 10

    def trueformed(self):
        
        trueformmessage = "It's time"
        for i in range(4):
            dots = "." * i
            sys.stdout.write(f"\r{trueformmessage}{dots}    ")

            sys.stdout.flush()
            time.sleep(1)

        time.sleep(1)

        print("MY TRUE FORM SHALL BE REVEALED!!!!")
        time.sleep(4)
        self.trueform = True


    def takedamage(self, damage):
        self.hpstat -= damage
        time.sleep(2)
        print(f"\nRAH takes {damage} damage.\n")
        time.sleep(2)
        print(f"RAH's HP = {self.hpstat}\n")
        time.sleep(2)

        if self.hpstat <= 0:
            self.isalive = False

        if self.isalive == False:
            print("RAH died brah\n") #placeholder for death cutscene or smth
            time.sleep(2)


    def bleeding_apply(self, duration=2):
            self.bleed = True
            self.bleed_duration = duration
            time.sleep(2)
            print('\nRAH starts bleeding.')
            time.sleep(2)


    def processbleeding(self):

        if self.bleed == True:
            self.hpstat -= 2 
            self.bleed_duration -= 1
            print(f"\nRAH took 2 bleed damage ({self.bleed_duration} left)")
            time.sleep(2)

            if self.bleed_duration <= 0:
                print(f"\nRAH took 2 bleed damage ({self.bleed_duration} left)")
                time.sleep(2)
                self.hpstat -= 2
                self.bleed = False
                print("\nRAH stops bleeding.")
                time.sleep(2)
        
            if self.hpstat <= 0:
                self.isalive = False






















