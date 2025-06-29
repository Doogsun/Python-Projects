class Goblin:

    def __init__ (self, level, hpstat):
        self.level = level
        self.hpstat = hpstat
        hpstat + level = hpstat

    def goblin_punch(self, level):
        print("A lowly growl crawls out of the green baby... a wild haymaker gets thrown thrown at you.  ")
        #hp -= 1 

    def goblin_smash(self, level, hpstat):
        print("A a disgruntled scowl forms on the green baby... With a leap into the air, a set of green fists fly towards you.")
        #hp -= 2 
        

    def goblin_fury(self, level, hpstast):
        print('Fury build within the green baby... A cascade of low slashes sweep your ankles.')
        #hp -=3
        #bleeding = True


    def goblin_evolve(self, level, hpstat ):
        print("GRAVITY HAS BROUGHT ME HERE FOR A REASON... THE STARS HAVE ALIGNED!!! THE TIME OF EVOLUTION IS NOW!!!")
        #become made in heaven and kill everyone