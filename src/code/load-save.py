from classes import Full_Caster
import csv

your_character = Full_Caster("Wizard", 1, 1, 1, 1, 1)

data = {
        "dndclass": your_character.dndclass,
        "level": your_character.level,
        "cantrips_known": your_character.cantrips_known,
        "level_1_spellslots": your_character.level_1_spellslots,
        "level_1_remaining": your_character.level_1_remaining,
        "level_2_spellslots": your_character.level_2_spellslots,
        "level_2_remaining": your_character.level_2_remaining,
        "level_3_spellslots": your_character.level_3_spellslots,
        "level_3_remaining": your_character.level_3_remaining,
        "level_4_spellslots": your_character.level_4_spellslots,
        "level_4_remaining": your_character.level_4_remaining,
        "level_5_spellslots": your_character.level_5_spellslots,
        "level_5_remaining": your_character.level_5_remaining,
        "level_6_spellslots": your_character.level_6_spellslots,
        "level_6_remaining": your_character.level_6_remaining,
        "level_7_spellslots": your_character.level_7_spellslots,
        "level_7_remaining": your_character.level_7_remaining,
        "level_8_spellslots": your_character.level_8_spellslots,
        "level_8_remaining": your_character.level_8_remaining,
        "level_9_spellslots": your_character.level_9_spellslots,
        "level_9_remaining": your_character.level_9_remaining,
}

loaded_data = []

def save_character():
    with open("your_character_file.csv", 'w') as your_character_file:
        writer = csv.DictWriter(your_character_file, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)

def load_character():
    your_character = Full_Caster("Blank", 0)
    with open ('your_character_file.csv', 'r') as your_character_file:
        heading = next(your_character_file)
        reader = csv.reader(your_character_file)
        for row in reader:
            loaded_data = row
    your_character.dndclass = loaded_data[0]
    your_character.level = int(loaded_data[1])
    your_character.cantrips_known = int(loaded_data[2])
    your_character.level_1_spellslots = int(loaded_data[3])
    your_character.level_1_remaining = int(loaded_data[4])
    your_character.level_2_spellslots = int(loaded_data[5])
    your_character.level_2_remaining = int(loaded_data[6])
    your_character.level_3_spellslots = int(loaded_data[7])
    your_character.level_3_remaining = int(loaded_data[8])
    your_character.level_4_spellslots = int(loaded_data[9])
    your_character.level_4_remaining = int(loaded_data[10])
    your_character.level_5_spellslots = int(loaded_data[11])
    your_character.level_5_remaining = int(loaded_data[12])
    your_character.level_6_spellslots = int(loaded_data[13])
    your_character.level_6_remaining = int(loaded_data[14])
    your_character.level_7_spellslots = int(loaded_data[15])
    your_character.level_7_remaining = int(loaded_data[16])
    your_character.level_8_spellslots = int(loaded_data[17])
    your_character.level_8_remaining = int(loaded_data[18])
    your_character.level_9_spellslots = int(loaded_data[19])
    your_character.level_9_remaining = int(loaded_data[20])
    print(your_character.dndclass)
    print(your_character.level)
    input("Enter to continue")
    return your_character

save_character()
load_character()
