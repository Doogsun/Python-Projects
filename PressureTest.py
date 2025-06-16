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
            print("\nair pressure units (pa, bar, torr, psi, atm)")
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
        print("\nair pressure units (pa, bar, torr, psi, atm)")
        time.sleep(1)
        convert_to = str(input("What would you like to convert it to?: ")).upper()

        if convert_to in units:
            unit_convert = units[convert_to]
            bleh2 = False
            return unit_convert
        
        else:
            print('\nPlease enter a correct unit of pressure')

        



def unit_conversion(value, ogunit, converto):
    print()





def main():
    output_list = prompting()
    unit_convert = prompting2()
    og_value = output_list['value']
    og_unit = output_list['originalunit']
    unit_conversion(og_value, og_unit, unit_convert)
  
    


if __name__ == "__main__":
    main()

    