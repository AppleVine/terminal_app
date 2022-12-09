
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
    

class SpellSlot():
    def __init__(self,maximum, remaining):
        self.maximum = maximum
        self.remaining = remaining

   

Character = Wizard(1, 1, 2, 3)

print(Character.level_1_spellslots.maximum)
print(Character.level_1_spellslots.remaining)