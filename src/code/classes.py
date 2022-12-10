from os import system
from functions import *

class SpellSlot():
    def __init__(self,available, consumed = 0):
        self.slots = available
        self.consumed = consumed

    def consume(self, value = 1):
        self.consume += value

class Wizard: 
    def __init__(self, level = 0, cantrips_known = 0, level_1_spellslots = 0, level_2_spellslots = 0, level_3_spellslots = 0, level_4_spellslots = 0, level_5_spellslots = 0, level_6_spellslots = 0, level_7_spellslots = 0, level_8_spellslots = 0, level_9_spellslots = 0,):
        self.level = level
        self.cantrips_known = cantrips_known
        self.level_1_spellslots = SpellSlot(level_1_spellslots)
        self.level_2_spellslots = SpellSlot(level_2_spellslots)
        self.level_3_spellslots = SpellSlot(level_3_spellslots)
        self.level_4_spellslots = level_4_spellslots
        self.level_5_spellslots = level_5_spellslots
        self.level_6_spellslots = level_6_spellslots
        self.level_7_spellslots = level_7_spellslots
        self.level_8_spellslots = level_8_spellslots
        self.level_9_spellslots = level_9_spellslots
        
level_1_wizard = 
level_2_wizard = 
level_3_wizard = 
level_4_wizard = Wizard(4, 4, 4, 3)
level_5_wizard = Wizard(5, 4, 4, 3, 2)
level_6_wizard = Wizard(6, 4, 4, 3, 3)
level_7_wizard = Wizard(7, 4, 4, 3, 3, 1)
level_8_wizard = Wizard(8, 4, 4, 3, 3, 2)
level_9_wizard = Wizard(9, 4, 4, 3, 3, 3, 1)
level_10_wizard = Wizard(10, 5, 4, 3, 3, 3, 2)
level_11_wizard = Wizard(11, 5, 4, 3, 3, 3, 2, 1)
level_12_wizard = Wizard(12, 5, 4, 3, 3, 3, 2, 1)
level_13_wizard = Wizard(13, 5, 4, 3, 3, 3, 2, 1, 1)
level_14_wizard = Wizard(14, 5, 4, 3, 3, 3, 2, 1, 1)
level_15_wizard = Wizard(15, 5, 4, 3, 3, 3, 2, 1, 1, 1)
level_16_wizard = Wizard(16, 5, 4, 3, 3, 3, 2, 1, 1, 1)
level_17_wizard = Wizard(17, 5, 4, 3, 3, 3, 2, 1, 1, 1, 1)
level_18_wizard = Wizard(18, 5, 4, 3, 3, 3, 3, 1, 1, 1, 1)
level_19_wizard = Wizard(19, 5, 4, 3, 3, 3, 3, 2, 1, 1, 1)
level_20_wizard = Wizard(20, 5, 4, 3, 3, 3, 3, 2, 2, 1, 1)

character = Wizard(0)

def get_wizard_level():
    input_level = 0
    # global your_character
    # your_character = Wizard(0)
    while input_level != "quit":
        system('clear')
        input_level = input("What level is your Wizard? ")
        system('clear')
        if input_level == "quit":
            quit()
        elif input_level == "1":
            your_character = Wizard(1, 3, 2)
            return your_character
        elif input_level == "2":
            your_character = Wizard(2, 3, 3)
            return your_character
        # elif input_level == "3":
        #     your_character = level_3_wizard
        #     return your_character
        # elif input_level == "4":
        #     your_character = level_4_wizard
        #     return your_character
        # elif input_level == "5":
        #     your_character = level_5_wizard
        #     return your_character
        # elif input_level == "6":
        #     your_character = level_6_wizard
        #     return your_character
        # elif input_level == "7":
        #     your_character = level_7_wizard
        #     return your_character
        # elif input_level == "8":
        #     your_character = level_8_wizard
        #     return your_character
        # elif input_level == "9":
        #     your_character = level_9_wizard
        #     return your_character
        # elif input_level == "10":
        #     your_character = level_10_wizard
        #     return your_character
        # elif input_level == "11":
        #     your_character = level_11_wizard
        #     return your_character
        # elif input_level == "12":
        #     your_character = level_12_wizard
        #     return your_character
        # elif input_level == "13":
        #     your_character = level_13_wizard
        #     return your_character
        # elif input_level == "14":
        #     your_character = level_14_wizard
        #     return your_character
        # elif input_level == "15":
        #     your_character = level_15_wizard
        #     return your_character
        # elif input_level == "16":
        #     your_character = level_16_wizard
        #     return your_character
        # elif input_level == "17":
        #     your_character = level_17_wizard
        #     return your_character
        # elif input_level == "18":
        #     your_character = level_18_wizard
        #     return your_character
        # elif input_level == "19":
        #     your_character = level_19_wizard
        #     return your_character
        # elif input_level == "20":
        #     your_character = level_20_wizard
        #     return your_character
        else:
            print("That's not a valid option, please try again.")
            input("Enter to continue.")


class Paladin: 
    def __init__(self, level = 0, cantrips_known = 0, level_1_spellslots = 0, level_2_spellslots = 0, level_3_spellslots = 0, level_4_spellslots = 0, level_5_spellslots = 0, level_6_spellslots = 0, level_7_spellslots = 0, level_8_spellslots = 0, level_9_spellslots = 0,):
        self.level = level
        self.cantrips_known = cantrips_known
        self.level_1_spellslots = level_1_spellslots
        self.level_2_spellslots = level_2_spellslots
        self.level_3_spellslots = level_3_spellslots
        self.level_4_spellslots = level_4_spellslots
        self.level_5_spellslots = level_5_spellslots
        self.level_6_spellslots = level_6_spellslots
        self.level_7_spellslots = level_7_spellslots
        self.level_8_spellslots = level_8_spellslots
        self.level_9_spellslots = level_9_spellslots
    
level_1_paladin = Paladin(1)
level_2_paladin = Paladin(2, 0, 2)
level_3_paladin = Paladin(3, 0, 3)
level_4_paladin = Paladin(4, 0, 3)
level_5_paladin = Paladin(5, 0, 4, 2)
level_6_paladin = Paladin(6, 0, 4, 2)
level_7_paladin = Paladin(7, 0, 4, 3)
level_8_paladin = Paladin(8, 0, 4, 3)
level_9_paladin = Paladin(9, 0, 4, 3, 2)
level_10_paladin = Paladin(10, 0, 4, 3, 2)
level_11_paladin = Paladin(11, 0, 4, 3, 3)
level_12_paladin = Paladin(12, 0, 4, 3, 3)
level_13_paladin = Paladin(13, 0, 4, 3, 3, 1)
level_14_paladin = Paladin(14, 0, 4, 3, 3, 1)
level_15_paladin = Paladin(15, 0, 4, 3, 3, 2)
level_16_paladin = Paladin(16, 0, 4, 3, 3, 2)
level_17_paladin = Paladin(17, 0, 4, 3, 3, 3, 1)
level_18_paladin = Paladin(18, 0, 4, 3, 3, 3, 1)
level_19_paladin = Paladin(19, 0, 4, 3, 3, 3, 2)
level_20_paladin = Paladin(20, 0, 4, 3, 3, 3, 2)

def get_paladin_level():
    input_level = 0
    while input_level != "quit":
        system('clear')
        input_level = input("What level is your Paladin? ")
        system('clear')
        if input_level == "quit":
            quit()
        elif input_level == "1":
            return Paladin(1)
        elif input_level == "2":
            return Paladin(2, 0, 2)
        # elif input_level == "3":
        #     your_character = level_3_paladin
        #     return your_character
        # elif input_level == "4":
        #     your_character = level_4_paladin
        #     return your_character
        # elif input_level == "5":
        #     your_character = level_5_paladin
        #     return your_character
        # elif input_level == "6":
        #     your_character = level_6_paladin
        #     return your_character
        # elif input_level == "7":
        #     your_character = level_7_paladin
        #     return your_character
        # elif input_level == "8":
        #     your_character = level_8_paladin
        #     return your_character
        # elif input_level == "9":
        #     your_character = level_9_paladin
        #     return your_character
        # elif input_level == "10":
        #     your_character = level_10_paladin
        #     return your_character
        # elif input_level == "11":
        #     your_character = level_11_paladin
        #     return your_character
        # elif input_level == "12":
        #     your_character = level_12_paladin
        #     return your_character
        # elif input_level == "13":
        #     your_character = level_13_paladin
        #     return your_character
        # elif input_level == "14":
        #     your_character = level_14_paladin
        #     return your_character
        # elif input_level == "15":
        #     your_character = level_15_paladin
        #     return your_character
        # elif input_level == "16":
        #     your_character = level_16_paladin
        #     return your_character
        # elif input_level == "17":
        #     your_character = level_17_paladin
        #     return your_character
        # elif input_level == "18":
        #     your_character = level_18_paladin
        #     return your_character
        # elif input_level == "19":
        #     your_character = level_19_paladin
        #     return your_character
        # elif input_level == "20":
        #     your_character = level_20_paladin
        #     return your_character
        else:
            print("That's not a valid option, please try again.")
            input("Enter to continue.")

def get_character():
    print("Please enter in your class from the following choices: ")
    selection = input("Paladin \nWizard\n")
    system('clear')
    if selection == "quit":
        quit()
    elif selection == "Paladin":
        get_paladin_level()
        print(your_character.level_1_spellslots)
        return your_character
    elif selection == "Wizard":
        get_wizard_level()
        print(your_character.level_1_spellslots)
        return your_character
