import csv

with open ('your_character_file.csv', 'r') as your_character_file:
    csv_reader = csv.reader(your_character_file)

    for line in csv_reader:
        print(line)


with open("your_character_file.csv", 'w') as your_character_file:
    csv_writer = csv.writer(your_character_file)


Class, level, cantrips_known, level_1_spellslots, level_1_remaining, level_2_spellslots, level_2_remaining, level_3_spellslots, level_3_remaining, level_4_spellslots, level_4_remaining, level_5_spellslots, level_5_remaining, level_6_spellslots, level_6_remaining, level_7_spellslots, level_7_remaining, level_8_spellslots, level_8_remaining, level_9_spellslots, level_9_remaining,
Wizard, 10, 8, 3, 4, 5,