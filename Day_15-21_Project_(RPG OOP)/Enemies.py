import random
import time
import sys

class Goblin:

    def __init__ (self, level, hpstat):

        self.level = level
        self.hpstat = hpstat + (2 * level)
        if hpstat > 0:
            self.isalive = True

        self.evovled = False

        



    def choose_move(self):
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

        if 1 <= goblinmove <= 53:
            self.punch()
            return 1

        if 54 <= goblinmove <= 76:
            self.smash()
            return 2
    
        if 77 <= goblinmove < 97:
            self.fury()
            return 3
            #bleeding

        if goblinmove in (97, 98, 99, 100):
            self.evolve()
            return 0
            



    def punch(self):
        print("\nA lowly growl crawls out of the green baby... a wild haymaker gets thrown thrown at you.")
        #hp -= 1 

    def smash(self):
        print("\nA a disgruntled scowl forms on the green baby... With a leap into the air, a set of green fists fly towards you.")
        #hp -= 2 
        

    def fury(self):
        print('\nFury build within the green baby... A cascade of low slashes sweep your ankles.')
        #hp -=3
        #bleeding = True


    def evolve(self):

        print("\nGRAVITY HAS BROUGHT ME HERE FOR A REASON... THE STARS HAVE ALIGNED!!! THE TIME OF EVOLUTION IS NOW!!!")
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

        if self.hpstat < 0:
            self.isalive = False

        if self.isalive == False:
            print("The goblin died\n") #placeholder for death cutscene or smth
            time.sleep(2)


class Golem:

    def __init__(self, level, hpstat):
        self.level = level
        self.hpstat = hpstat + (2 * level)
        if hpstat > 0:
            self.isalive = True


    def choose_move(self):
        golemmove = random.randint(1,100)
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

        if 1 <= golemmove <= 43:
            self.strongleft()
            return 2

        if 44 <= golemmove <= 66:
            self.breakercombo()
            return 4
    
        if 67 <= golemmove <= 87:
            self.thunderclap()
            return 3
            #concussed
            

        if  88 <= golemmove <= 100:
            self.grug()
            return 0 



    def strongleft(self):
        print("\nThe grinding of stone against stone... The hunkering mass of stone fires a crushing vortex from his left arm. ")
        #hp -= 2
    
    def breakercombo(self):
        print("\nA fierece wind surronds the hailing stone... RIGHT, LEFT, RIGHT, LEFT. Rapid Punches.. ")
        #hp -= 4 

    def thunderclap(self):
        print("\nThe ground begins to rumble.. The rock mass slams his fists together, creating a thundering shockwave.")
        #hp -= 3 
        #concussed

    def grug(self):
        print("\nStones shake and recover... Grug. Gruggy Grug 🪨")
        self.hpstat += 7


    def takedamage(self, damage):
        self.hpstat -= damage
        time.sleep(2)
        print(f"\nThe Golem took {damage} damage.\n")
        time.sleep(2)
        print(f"The Golem's HP = {self.hpstat}\n")
        time.sleep(2)

        if self.hpstat < 0:
            self.isalive = False

        if self.isalive == False:
            print("The golem died\n") #placeholder for death cutscene or smth
            time.sleep(2)
    

class RAH:

    def __init__(self, level, hpstat):
        self.level = level
        self.hpstat = hpstat + (2 * level)
        if hpstat > 0:
            self.isalive = True

        self.trueform = False



    def choose_move(self):
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

        if rahmove == 1:
            self.trueformed()
            return 0

        if 2 <= rahmove <= 43:
            self.Ray_Of_Sun()
            return 2

        if 44 <= rahmove <= 66:
            self.Solar_shards()
            return 4
    
        if 67 <= rahmove <= 87:
            self.Bolts_of_RAH()
            return 3
            #thunderclaped
            
        if  88 <= rahmove <= 100:
            self.RAHWARTH()
            return 10



    def Ray_Of_Sun(self):
        print('A Precense of Divine Acuity Shines down on you... "YOU SHALL OBEY!! ')
        #hpstat -= 3

    def Bolts_of_RAH(self):
        print("The a temporary eclispe blocks the sky... Pillars of light rain down on you")
        #hpstat -= 4
        #concussed = True

    def Solar_shards(self):
        print('"HA HA HA!!!"... A shattered star-shards of torment!')
        #hpstat -= 3
        #bleeding = True

    def RAHWARTH(self):
        print("Thats it... Its over for you.... Bleh! :p")
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

        if self.hpstat < 0:
            self.isalive = False

        if self.isalive == False:
            print("RAH died brah\n") #placeholder for death cutscene or smth
            time.sleep(2)


























