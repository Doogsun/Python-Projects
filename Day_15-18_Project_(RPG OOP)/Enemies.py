class Goblin:

    def __init__ (self, level, hpstat):

        self.level = 1 + level
        self.hpstat = 1 + hpstat
        if hpstat > 0:
            self.isalive = True


    def punch(self):
        print("A lowly growl crawls out of the green baby... a wild haymaker gets thrown thrown at you.")
        #hp -= 1 

    def smash(self):
        print("\nA a disgruntled scowl forms on the green baby... With a leap into the air, a set of green fists fly towards you.")
        #hp -= 2 
        

    def fury(self):
        print('Fury build within the green baby... A cascade of low slashes sweep your ankles.')
        #hp -=3
        #bleeding = True


    def evolve(self):
        print("GRAVITY HAS BROUGHT ME HERE FOR A REASON... THE STARS HAVE ALIGNED!!! THE TIME OF EVOLUTION IS NOW!!!")
        #become made in heaven and kill everyone



class Golem:

    def __init__(self, level, hpstat):
        self.level = 1 + level
        self.hpstat = 1 + hpstat
        if hpstat > 0:
            self.isalive = True

    def strongleft(self):
        print("The grinding of stone against stone... The hunkering mass of stone fires a crushing vortex from his left arm. ")
        #hp -= 2
    
    def breakercombo(self):
        print("A fierece wind surronds the hailing stone... RIGHT, LEFT, RIGHT, LEFT. Rapid Punches.. ")
        #hp -= 4 

    def thunderclap(self):
        print("The ground begins to rumble.. The rock mass slams his fists together, creating a thundering shockwave.")
        #hp -= 3 
        #concussed

    def grug(self):
        print("Stones shake and recover... Grug. Gruggy Grug 🪨")
        #hp += 2



class RAH:

    def __init__(self, level, hpstat):
        self.level = level
        self.hpstat = hpstat
        if hpstat > 0:
            self.isalive = True

    def Ray_Of_Sun(self):
        print('A Precense of Divine Acuity Shines down on you... "YOU SHALL OBEY!! ')
        #hpstat -= 3

    def Bolts_of_RAH(self):
        print("The a temporary eclispe blocks the sky... Pillars of light rain down on you")
        #hpstat -= 4
        #sunned = True

    def Solar_shards(self):
        print('"HA HA HA!!!"... A shattered star-shards of torment!')
        #hpstat -= 3
        #bleeding = True

    def RAHWARTH(self):
        print("Thats it... Its over for you.... Bleh! :p")
        #hpstat -= 10































goblin1 = Goblin(5, 10)
print(goblin1.level, goblin1.hpstat)