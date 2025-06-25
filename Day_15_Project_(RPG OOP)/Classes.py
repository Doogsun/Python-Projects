class Warrior:

    def __init__(self, strstat, hpstat):

        self.strstat = strstat
        self.hpstat = hpstat

        

    def basic_atk(self):
        print("\nWith a hefty swing of ol-betsy... you slash at your opponent\n")
        enemyhp -= 2 

    def warriors_serrate(self):
        print("\nol-betsy stances up... a swift dual slash grates your opponent")
        enemyhp -= 2
        bleeding = True



class Wizard:

    def __init__(self, arcstat, hpstat):
        
        self.arcstat = arcstat
        self.hpstat = hpstat

    def basic_atk(self):
        print("Magic pools around you.. You send an arcane bolt at your opponent ")
        enemyhp -= 2 

    def magic_rain(self):
        print("Magic surges into the sky.. You rain spiked shards of arcane down onto your opponent")
        enemyhp -= 2
        bleeding = True



class Rogue:

    def __init__(self, dexstat, hpstat):

        self.dexstat = dexstat
        self.hpstat = hpstat

    def basic_atk(self):
        print("A wisp of a robe is heard.. You execute a smooth, in and out slice with your dagger")
        enemyhp -= 2 

    def ankle_cutter(self):
        print("A shadow slids across the floor.. You slash at your opponents ankles")
        enemyhp -= 2
        bleeding = True