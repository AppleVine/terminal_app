from os import system

your_character = None

class Wizard: 
    def __init__(self, level = 0, cantrips_known = 0, level_1_spellslots = 0, level_1_remaining = 0, level_2_spellslots = 0, level_2_remaining = 0, level_3_spellslots = 0, level_3_remaining = 0, 
    level_4_spellslots = 0, level_4_remaining = 0, level_5_spellslots = 0, level_5_remaining = 0, level_6_spellslots = 0, level_6_remaining = 0, level_7_spellslots = 0, level_7_remaining = 0, 
    level_8_spellslots = 0, level_8_remaining = 0, level_9_spellslots = 0, level_9_remaining = 0):
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
    
class Paladin: 
    def __init__(self, level = 0, cantrips_known = 0, level_1_spellslots = 0, level_1_remaining = 0, level_2_spellslots = 0, level_2_remaining = 0, level_3_spellslots = 0, level_3_remaining = 0, 
    level_4_spellslots = 0, level_4_remaining = 0, level_5_spellslots = 0, level_5_remaining = 0, level_6_spellslots = 0, level_6_remaining = 0, level_7_spellslots = 0, level_7_remaining = 0, 
    level_8_spellslots = 0, level_8_remaining = 0, level_9_spellslots = 0, level_9_remaining = 0):
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
    

def get_wizard_level():
    input_level = 0
    your_character = None
    while input_level != "quit":
        system('clear')
        input_level = input("What level is your Wizard? ")
        system('clear')
        if input_level == "quit":
            quit()
        elif input_level == "1":
            your_character = Wizard(1, 3, 2, 2)
            return your_character
        elif input_level == "2":
            your_character = Wizard(2, 3, 3, 3)
            return your_character
        elif input_level == "3":
            your_character = Wizard(3, 3, 4, 4, 2, 2)
            return your_character
        elif input_level == "4":
            your_character = Wizard(4, 4, 4, 4, 3, 3)
            return your_character
        elif input_level == "5":
            your_character = Wizard(5, 4, 4, 4, 3, 3, 2, 2)
            return your_character
        elif input_level == "6":
            your_character = Wizard(6, 4, 4, 4, 3, 3, 3, 3)
            return your_character
        elif input_level == "7":
            your_character = Wizard(7, 4, 4, 4, 3, 3, 3, 3, 1, 1)
            return your_character
        elif input_level == "8":
            your_character = Wizard(8, 4, 4, 4, 3, 3, 3, 3, 2, 2)
            return your_character
        elif input_level == "9":
            your_character = Wizard(9, 4, 4, 4, 3, 3, 3, 3, 3, 3, 1, 1)
            return your_character
        elif input_level == "10":
            your_character = Wizard(10, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2)
            return your_character
        elif input_level == "11":
            your_character = Wizard(11, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1)
            return your_character
        elif input_level == "12":
            your_character = Wizard(12, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1)
            return your_character
        elif input_level == "13":
            your_character = Wizard(13, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1)
            return your_character
        elif input_level == "14":
            your_character = Wizard(14, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1)
            return your_character
        elif input_level == "15":
            your_character = Wizard(15, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1)
            return your_character
        elif input_level == "16":
            your_character = Wizard(16, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1)
            return your_character
        elif input_level == "17":
            your_character = Wizard(17, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1)
            return your_character
        elif input_level == "18":
            your_character = Wizard(18, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1)
            return your_character
        elif input_level == "19":
            your_character = Wizard(19, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1)
            return your_character
        elif input_level == "20":
            your_character = Wizard(20, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1)
            return your_character
        else:
            print("That's not a valid option, please try again.")
            input("Enter to continue.")


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
        elif input_level == "3":
            your_character = Paladin(3, 0, 3)
            return your_character
        elif input_level == "4":
            your_character = Paladin(4, 0, 3)
            return your_character
        elif input_level == "5":
            your_character = Paladin(5, 0, 4, 2)
            return your_character
        elif input_level == "6":
            your_character = Paladin(6, 0, 4, 2)
            return your_character
        elif input_level == "7":
            your_character = Paladin(7, 0, 4, 3)
            return your_character
        elif input_level == "8":
            your_character = Paladin(8, 0, 4, 3)
            return your_character
        elif input_level == "9":
            your_character = Paladin(9, 0, 4, 3, 2)
            return your_character
        elif input_level == "10":
            your_character = Paladin(10, 0, 4, 3, 2)
            return your_character
        elif input_level == "11":
            your_character = Paladin(11, 0, 4, 3, 3)
            return your_character
        elif input_level == "12":
            your_character = Paladin(12, 0, 4, 3, 3)
            return your_character
        elif input_level == "13":
            your_character = Paladin(13, 0, 4, 3, 3, 1)
            return your_character
        elif input_level == "14":
            your_character = Paladin(14, 0, 4, 3, 3, 1)
            return your_character
        elif input_level == "15":
            your_character = Paladin(15, 0, 4, 3, 3, 2)
            return your_character
        elif input_level == "16":
            your_character = Paladin(16, 0, 4, 3, 3, 2)
            return your_character
        elif input_level == "17":
            your_character = Paladin(17, 0, 4, 3, 3, 3, 1)
            return your_character
        elif input_level == "18":
            your_character = Paladin(18, 0, 4, 3, 3, 3, 1)
            return your_character
        elif input_level == "19":
            your_character = Paladin(19, 0, 4, 3, 3, 3, 2)
            return your_character
        elif input_level == "20":
            your_character = Paladin(20, 0, 4, 3, 3, 3, 2)
            return your_character
        else:
            print("That's not a valid option, please try again.")
            input("Enter to continue.")



def get_character():
    print("Please enter in your class from the following choices: ")
    class_selection = input("Paladin \nWizard\n \n-------- \n \n")
    system('clear')
    if class_selection == "quit":
        quit()
    elif class_selection == "Paladin":
        your_character = get_paladin_level()
        print(your_character.level_1_spellslots)
        input("Character successfully created. Please press enter to return to main menu. \n \n-------- \n \n")
        return your_character
    elif class_selection == "Wizard":
        your_character = get_wizard_level()
        print(your_character.level_1_spellslots)
        input("Character successfully created. Please press enter to return to main menu.\n \n-------- \n \n")
        return your_character
