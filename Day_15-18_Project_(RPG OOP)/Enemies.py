class Goblin:


    def __init__ (self, level, hpstat):

        self.level = 1 + level
        self.hpstat = 1 + hpstat
        if hpstat > 0:
            self.isalive = True

   

    def punch(self):
        print("\nA lowly growl crawls out of the green baby... a wild haymaker gets thrown thrown at you.\n")
        #hp -= 1 

    def smash(self):
        print("\nA a disgruntled scowl forms on the green baby... With a leap into the air, a set of green fists fly towards you.\n")
        #hp -= 2 
        

    def fury(self):
        print('\nFury build within the green baby... A cascade of low slashes sweep your ankles.\n')
        #hp -=3
        #bleeding = True


    def evolve(self):
        print("\nGRAVITY HAS BROUGHT ME HERE FOR A REASON... THE STARS HAVE ALIGNED!!! THE TIME OF EVOLUTION IS NOW!!!\n")
        #become made in heaven and kill everyone

goblin1 = Goblin(5, 10)
print(goblin1.level, goblin1.hpstat)