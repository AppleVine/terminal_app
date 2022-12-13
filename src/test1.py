import csv

your_character = None

class Wizard: 
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

your_character = Wizard(15, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1)

data = {
    "dndclass": your_character.dndclass,
    "level": your_character.level,
    "cantrips_known": your_character.cantrips_known,
    "level_1_spellslots": your_character.level_1_spellslots,
    "level_1_remaining": your_character.level_1_remaining,
}


def save_character():
    with open("your_character_file.csv", 'w') as your_character_file:
        writer = csv.DictWriter(your_character_file, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)




# with open ('your_character_file.csv', 'r') as your_character_file:
#     csv_reader = csv.reader(your_character_file)

#     for line in csv_reader:
#         print(line)

