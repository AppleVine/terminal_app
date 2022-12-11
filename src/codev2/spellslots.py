

def use_spell(your_character):
    spell_selection = input("What level spellslot are you using?")
    if spell_selection == "1":
        if your_character.level_1_remaining <= 1:
            your_character.level_1_remaining -= 1
            return your_character
        else:
            print("You do not have enough spell slots remaining. You need to rest first!")
    elif spell_selection == "2":
        if your_character.level_2_remaining <= 1:
            your_character.level_2_remaining -= 1
            return your_character
        else:
            print("You do not have enough spell slots remaining. You need to rest first!")
    elif spell_selection == "3":
        if your_character.level_3_remaining <= 1:
            your_character.level_3_remaining -= 1
            return your_character
        else:
            print("You do not have enough spell slots remaining. You need to rest first!")
    elif spell_selection == "4":
        if your_character.level_4_remaining <= 1:
            your_character.level_4_remaining -= 1
            return your_character
        else:
            print("You do not have enough spell slots remaining. You need to rest first!")
    elif spell_selection == "5":
        if your_character.level_5_remaining <= 1:
            your_character.level_5_remaining -= 1
            return your_character
        else:
            print("You do not have enough spell slots remaining. You need to rest first!")
    elif spell_selection == "6":
        if your_character.level_6_remaining <= 1:
            your_character.level_6_remaining -= 1
            return your_character
        else:
            print("You do not have enough spell slots remaining. You need to rest first!")
    elif spell_selection == "7":
        if your_character.level_7_remaining <= 1:
            your_character.level_7_remaining -= 1
            return your_character
        else:
            print("You do not have enough spell slots remaining. You need to rest first!")
    elif spell_selection == "8":
        if your_character.level_8_remaining <= 1:
            your_character.level_8_remaining -= 1
            return your_character
        else:
            print("You do not have enough spell slots remaining. You need to rest first!")
    elif spell_selection == "9":
        if your_character.level_9_remaining <= 1:
            your_character.level_9_remaining -= 1
            return your_character
        else:
            print("You do not have enough spell slots remaining. You need to rest first!")

class Wizard: 
    def __init__(self, level = 0, cantrips_known = 0, level_1_spellslots = 0, level_1_remaining = 0, level_2_spellslots = 0, level_2_remaining = 0, level_3_spellslots = 0, level_4_spellslots = 0, level_5_spellslots = 0, level_6_spellslots = 0, level_7_spellslots = 0, level_8_spellslots = 0, level_9_spellslots = 0,):
        self.level = level
        self.cantrips_known = cantrips_known
        self.level_1_spellslots = level_1_spellslots
        self.level_1_remaining = level_1_remaining
        self.level_2_spellslots = level_2_spellslots
        self.level_2_remaining = level_2_remaining
        self.level_3_spellslots = level_3_spellslots

        self.level_4_spellslots = level_4_spellslots

        self.level_5_spellslots = level_5_spellslots

        self.level_6_spellslots = level_6_spellslots

        self.level_7_spellslots = level_7_spellslots

        self.level_8_spellslots = level_8_spellslots

        self.level_9_spellslots = level_9_spellslots
    
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