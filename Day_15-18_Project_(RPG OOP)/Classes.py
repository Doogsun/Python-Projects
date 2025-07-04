class Warrior:

    def __init__(self, strstat, hpstat):

        self.strstat = strstat
        self.hpstat = hpstat
        if hpstat > 0:
            self.isalive = True
        

    def basic_atk(self):
        print("With a hefty swing of ol-betsy.. you slash at your opponent.")
        #enemyhp -= 2 

    def warriors_serrate(self):
        print("\nol-betsy stances up.. a swift dual slash grates your opponent.")
        #enemyhp -= 2
        #bleeding = True


    def pommel_strike(self):
        print("A swole power enters your arm.. You club they beast over the head with your swords pommel.")
        #enemyhp -=3

    def whirlwind_spin(self):
        print("A vortex of wind empowers you.. You unleash a reckless flury of spining slashes.")




class Wizard:

    def __init__(self, arcstat, hpstat):
        
        self.arcstat = arcstat
        self.hpstat = hpstat
        if hpstat > 0:
            self.isalive = True

    def basic_atk(self):
        print("Magic pools around you.. You send an arcane bolt at your opponent.")
        #enemyhp -= 2 

    def magic_rain(self):
        print("Magic surges into the sky.. You rain spiked shards of arcane down onto your opponent.")
        #enemyhp -= 2
        #bleeding = True

    def magic_crackers(self):
        print("Magic explodes into life.. A show of magical sparklers set your enemey a blaze.")


    def arcanus_pinnus(self):
        print("A large surge of magic converges into a small point.. A thin beam donut anything in its path.")



class Rogue:

    def __init__(self, dexstat, hpstat):

        self.dexstat = dexstat
        self.hpstat = hpstat
        if hpstat > 0:
            self.isalive = True

    def basic_atk(self):
        print("A wisp of a robe is heard.. You execute a smooth, in and out slice with your dagger.")
        #enemyhp -= 2 

    def ankle_cutter(self):
        print("A shadow slids across the floor.. You slash at your opponents ankles.")
        #enemyhp -= 2
        #bleeding = True

    def dropkick_slash(self):
        print('A phaseflicker shrouds your movement.. You appear above your oppoenent, meteoring down and slasshing them.')


    def thousand_flashstep(self):
        print("A flashstep slices through the air.. A flashtunnel of slashes sprials past your flashstep.")