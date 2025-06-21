#write a program that converts untis of gas pressure to other units of gas pressure
#Units: Pa (pascal), Bar (bar), psi (pounds per square inch), Torr (mmHg), atm (atmosphere of earth)

import time

units = {'PA':1, 'BAR':2, 'PSI':3, 'TORR':4, 'ATM':5  }

def prompting():
    bleh = True
    while bleh == True:
        try:
            time.sleep(1)
            orginal_value = float(input("Please enter a value of air pressure: "))
            time.sleep(1)
            print("\nair pressure units (Pa, Bar, Torr, Psi, atm)")
            time.sleep(1)
            orginal_unit = str(input("Please enter the unit of measurement for the value: ")).upper()

            if orginal_unit in units: 
                unit_value = units[orginal_unit]
                prompt_out = {"value":orginal_value, "originalunit":unit_value}
                bleh = False
                return prompt_out
                
            else:
                print('\nPlease enter a correct unit of pressure')

        except ValueError:
            print("\nPlease enter a valid format (1st = float, 2nd = str)")
            
        
def prompting2():
    bleh2 = True
    while bleh2:
        print("\nair pressure units (Pa, Bar, Torr, Psi, atm)")
        time.sleep(1)
        convert_to = str(input("What would you like to convert it to?: ")).upper()

        if convert_to in units:
            unit_convert = units[convert_to]
            bleh2 = False
            return unit_convert
        
        else:
            print('\nPlease enter a correct unit of pressure')

        

def unit_conversion(value, ogunit, converto):

    padict = {1:1, 2:10**-5, 3:0.000145038, 4:.00750062, 5:9.86923*10**-6}
    bardict = {1:100000, 2:1, 3:14.5038, 4:750.062, 5:0.986923}
    psidict = {1:6894.76, 2:0.0689476, 3:1, 4:51.7149, 5:0.068046}
    torrdict = {1:133.322, 2:0.00133322, 3:0.0193368, 4:1, 5:0.00131579}
    atmdict = {1:101325, 2:1.01325, 3:14.6959, 4:760, 5:1}
    
    if ogunit == 1:
        indexratio1 = padict[converto]
        return value * indexratio1
    if ogunit == 2:
        indexratio2 = bardict[converto]
        return value * indexratio2
    if ogunit == 3:
        indexratio3 = psidict[converto]
        return value * indexratio3
    if ogunit == 4:
        indexratio4 = torrdict[converto]
        return value * indexratio4
    if ogunit == 5:
        indexratio5 = atmdict[converto]
        return value * indexratio5


def final_msg(final, ogunit, unit_convert, ogvalue):
    units2 = {1:'Pa', 2:'Bar', 3:'Psi', 4:'Torr', 5:'atm'}
    returned_ogunit = units2[ogunit]
    returned_convert = units2[unit_convert]
    print("\nLoading Result!!! :3 .....")

    time.sleep(3)

    print(f"\nYou converted {ogvalue} {returned_ogunit} to {final} {returned_convert}!\n")
    

def main():
    output_list = prompting()
    unit_convert = prompting2()

    og_value = output_list['value']
    og_unit = output_list['originalunit']

    final_product = unit_conversion(og_value, og_unit, unit_convert)
    final_msg(final_product, og_unit, unit_convert, og_value)
    
    

if __name__ == "__main__":
    main()

    