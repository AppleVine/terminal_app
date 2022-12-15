from os import system


class Full_Caster: 
    def __init__(self, dndclass = "Wizard", level = 0, cantrips_known = 0, level_1_spellslots = 0, level_1_remaining = 0, level_2_spellslots = 0, level_2_remaining = 0, level_3_spellslots = 0, level_3_remaining = 0, 
    level_4_spellslots = 0, level_4_remaining = 0, level_5_spellslots = 0, level_5_remaining = 0, level_6_spellslots = 0, level_6_remaining = 0, level_7_spellslots = 0, level_7_remaining = 0, 
    level_8_spellslots = 0, level_8_remaining = 0, level_9_spellslots = 0, level_9_remaining = 0):
        self.dndclass = dndclass
        self.level = level  
        self.cantrips_known = cantrips_known
        self.level_1_spellslots = level_1_spellslots
        self.level_1_remaining = level_1_remaining
        self.level_2_spellslots = level_2_spellslots
        self.level_2_remaining = level_2_remaining
        self.level_3_spellslots = level_3_spellslots
        self.level_3_remaining = level_3_remaining
        self.level_4_spellslots = level_4_spellslots
        self.level_4_remaining = level_4_remaining
        self.level_5_spellslots = level_5_spellslots
        self.level_5_remaining = level_5_remaining
        self.level_6_spellslots = level_6_spellslots
        self.level_6_remaining = level_6_remaining
        self.level_7_spellslots = level_7_spellslots
        self.level_7_remaining = level_7_remaining
        self.level_8_spellslots = level_8_spellslots
        self.level_8_remaining = level_8_remaining
        self.level_9_spellslots = level_9_spellslots
        self.level_9_remaining = level_9_remaining
    
class Half_Caster: 
    def __init__(self, dndclass = "Paladin", level = 0, cantrips_known = 0, level_1_spellslots = 0, level_1_remaining = 0, level_2_spellslots = 0, level_2_remaining = 0, level_3_spellslots = 0, level_3_remaining = 0, 
    level_4_spellslots = 0, level_4_remaining = 0, level_5_spellslots = 0, level_5_remaining = 0, level_6_spellslots = 0, level_6_remaining = 0, level_7_spellslots = 0, level_7_remaining = 0, 
    level_8_spellslots = 0, level_8_remaining = 0, level_9_spellslots = 0, level_9_remaining = 0):
        self.dndclass = dndclass
        self.level = level
        self.cantrips_known = cantrips_known
        self.level_1_spellslots = level_1_spellslots
        self.level_1_remaining = level_1_remaining
        self.level_2_spellslots = level_2_spellslots
        self.level_2_remaining = level_2_remaining
        self.level_3_spellslots = level_3_spellslots
        self.level_3_remaining = level_3_remaining
        self.level_4_spellslots = level_4_spellslots
        self.level_4_remaining = level_4_remaining
        self.level_5_spellslots = level_5_spellslots
        self.level_5_remaining = level_5_remaining
        self.level_6_spellslots = level_6_spellslots
        self.level_6_remaining = level_6_remaining
        self.level_7_spellslots = level_7_spellslots
        self.level_7_remaining = level_7_remaining
        self.level_8_spellslots = level_8_spellslots
        self.level_8_remaining = level_8_remaining
        self.level_9_spellslots = level_9_spellslots
        self.level_9_remaining = level_9_remaining
    
your_character = Full_Caster(0)

def get_wizard_level():
    input_level = 0
    your_character = None
    while input_level != "quit":
        system('clear')
        input_level = input("What level is your Wizard?\n\n-------- \n\n")
        system('clear')
        if input_level == "quit":
            quit()
        elif input_level == "1":
            your_character = Full_Caster("Wizard", 1, 3, 2, 2)
            return your_character
        elif input_level == "2":
            your_character = Full_Caster("Wizard", 2, 3, 3, 3)
            return your_character
        elif input_level == "3":
            your_character = Full_Caster("Wizard", 3, 3, 4, 4, 2, 2)
            return your_character
        elif input_level == "4":
            your_character = Full_Caster("Wizard", 4, 4, 4, 4, 3, 3)
            return your_character
        elif input_level == "5":
            your_character = Full_Caster("Wizard", 5, 4, 4, 4, 3, 3, 2, 2)
            return your_character
        elif input_level == "6":
            your_character = Full_Caster("Wizard", 6, 4, 4, 4, 3, 3, 3, 3)
            return your_character
        elif input_level == "7":
            your_character = Full_Caster("Wizard", 7, 4, 4, 4, 3, 3, 3, 3, 1, 1)
            return your_character
        elif input_level == "8":
            your_character = Full_Caster("Wizard", 8, 4, 4, 4, 3, 3, 3, 3, 2, 2)
            return your_character
        elif input_level == "9":
            your_character = Full_Caster("Wizard", 9, 4, 4, 4, 3, 3, 3, 3, 3, 3, 1, 1)
            return your_character
        elif input_level == "10":
            your_character = Full_Caster("Wizard", 10, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2)
            return your_character
        elif input_level == "11":
            your_character = Full_Caster("Wizard", 11, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1)
            return your_character
        elif input_level == "12":
            your_character = Full_Caster("Wizard", 12, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1)
            return your_character
        elif input_level == "13":
            your_character = Full_Caster("Wizard", 13, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1)
            return your_character
        elif input_level == "14":
            your_character = Full_Caster("Wizard", 14, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1)
            return your_character
        elif input_level == "15":
            your_character = Full_Caster("Wizard", 15, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1)
            return your_character
        elif input_level == "16":
            your_character = Full_Caster("Wizard", 16, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1)
            return your_character
        elif input_level == "17":
            your_character = Full_Caster("Wizard", 17, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1)
            return your_character
        elif input_level == "18":
            your_character = Full_Caster("Wizard", 18, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1)
            return your_character
        elif input_level == "19":
            your_character = Full_Caster("Wizard", 19, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1)
            return your_character
        elif input_level == "20":
            your_character = Full_Caster("Wizard", 20, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1)
            return your_character
        else:
            print("That's not a valid option, please try again.")
            input("Enter to continue.\n\n-------- \n\n")


def get_paladin_level():
    input_level = 0
    your_character = None
    while your_character == None:
        try:
            system('clear')
            input_level = input("What level is your Paladin? Please choose from 1-20.\n\n-------- \n\n")
            system('clear')
            int_input = int(input_level)
            if int_input == 1:
                your_character = Half_Caster("Paladin", 1)
                return your_character
            elif int_input == 2:
                your_character = Half_Caster("Paladin", 2, 0, 2)
                return your_character
            elif int_input == 3:
                your_character = Half_Caster("Paladin", 3, 0, 3)
                return your_character
            elif int_input == 4:
                your_character = Half_Caster("Paladin", 4, 0, 3)
                return your_character
            elif int_input == 5:
                your_character = Half_Caster("Paladin", 5, 0, 4, 2)
                return your_character
            elif int_input == 6:
                your_character = Half_Caster("Paladin", 6, 0, 4, 2)
                return your_character
            elif int_input == 7:
                your_character = Half_Caster("Paladin", 7, 0, 4, 3)
                return your_character
            elif int_input == 8:
                your_character = Half_Caster("Paladin", 8, 0, 4, 3)
                return your_character
            elif int_input == 9:
                your_character = Half_Caster("Paladin", 9, 0, 4, 3, 2)
                return your_character
            elif int_input == 10:
                your_character = Half_Caster("Paladin", 10, 0, 4, 3, 2)
                return your_character
            elif int_input == 11:
                your_character = Half_Caster("Paladin", 11, 0, 4, 3, 3)
                return your_character
            elif int_input == 12:
                your_character = Half_Caster("Paladin", 12, 0, 4, 3, 3)
                return your_character
            elif int_input == 13:
                your_character = Half_Caster("Paladin", 13, 0, 4, 3, 3, 1)
                return your_character
            elif int_input == 14:
                your_character = Half_Caster("Paladin", 14, 0, 4, 3, 3, 1)
                return your_character
            elif int_input == 15:
                your_character = Half_Caster("Paladin", 15, 0, 4, 3, 3, 2)
                return your_character
            elif int_input == 16:
                your_character = Half_Caster("Paladin", 16, 0, 4, 3, 3, 2)
                return your_character
            elif int_input == 17:
                your_character = Half_Caster("Paladin", 17, 0, 4, 3, 3, 3, 1)
                return your_character
            elif int_input == 18:
                your_character = Half_Caster("Paladin", 18, 0, 4, 3, 3, 3, 1)
                return your_character
            elif int_input == 19:
                your_character = Half_Caster("Paladin", 19, 0, 4, 3, 3, 3, 2)
                return your_character
            elif int_input == 20:
                your_character = Half_Caster("Paladin", 20, 0, 4, 3, 3, 3, 2)
                return your_character
        except ValueError:
            input("That's not a valid response, please only enter a number from 1-20.\nPress Enter to continue.\n\n-------- \n\n")

class_selection = None

def class_input():
    print("Please enter in the class from the following choices: ")
    class_selection = input("Paladin \nWizard\n\n-------- \n\n")
    system('clear')
    return class_selection


def class_selector(class_selection):
    if class_selection == "quit":
        quit()
    elif class_selection == "Paladin":
        your_character = get_paladin_level()
        input("You successfully created a level " + str(your_character.level) + " " + your_character.dndclass + ".\nPlease press enter to return to main menu.\n\n-------- \n\n")
        return your_character
    elif class_selection == "Wizard":
        your_character = get_wizard_level()
        input("You successfully created a level " + str(your_character.level) + " " + your_character.dndclass + ".\nPlease press enter to return to main menu.\n\n-------- \n\n")
        return your_character


def get_character():
    class_selection = class_input()
    your_character = class_selector(class_selection)
    return your_character






