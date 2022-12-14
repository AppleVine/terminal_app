from os import system
from classes import *
import csv


def main_menu_options():
    print("To quit at any time, please type: quit")
    print("1: Input class selection, and class level.")
    print("2: Check available spellslots")
    print("3: Use a spell")
    print("4: Long rest")
    print("5: View spell database")
    print("6: Update character spell-list.")
    print("7: Recommend my next learned spell.")
    print("8: Save your character.")
    print("9: Settings.")
    main_menu_option = input("Enter your option: ")
    return main_menu_option

def main_menu(your_character):
    main_menu_selection = ""
    while main_menu_selection != "quit":
        system('clear')
        main_menu_selection = main_menu_options()
        system('clear')
        if main_menu_selection == "1":
            your_character = get_character()
        elif main_menu_selection == "2":
            get_spells(your_character)
        elif main_menu_selection == "3":
            use_spell(your_character)
        elif main_menu_selection == "4":
            rest(your_character)
        elif main_menu_selection == "5":
            print("This is option 5.")
            input("Press enter to return to the main menu.")
        elif main_menu_selection == "6":
            print("This is option 6.")
            input("Press enter to return to the main menu.")
        elif main_menu_selection == "7":
            print("This is option 7.")
            input("Press enter to return to the main menu.")
        elif main_menu_selection == "8":
            save_character(your_character)
            input("Your character has saved successfully.\nPress Enter to return to the main menu.\n\n-------- \n\n")
        elif main_menu_selection == "9":
            print("This is option 9.")
            input("Press enter to return to the main menu.")
        elif main_menu_selection == "quit":
            quit()
        else:
            print("Please only input the number you would like to select.\nPress Enter to return to the Main Menu.")

def get_spells(your_character):
    try:
        print("You have " + str(your_character.level_1_remaining) + " level 1 spellslots available.")
        print("You have " + str(your_character.level_2_remaining) + " level 2 spellslots available.")
        print("You have " + str(your_character.level_3_remaining) + " level 3 spellslots available.")
        print("You have " + str(your_character.level_4_remaining) + " level 4 spellslots available.")
        print("You have " + str(your_character.level_5_remaining) + " level 5 spellslots available.")
        print("You have " + str(your_character.level_6_remaining) + " level 6 spellslots available.")
        print("You have " + str(your_character.level_7_remaining) + " level 7 spellslots available.")
        print("You have " + str(your_character.level_8_remaining) + " level 8 spellslots available.")
        print("You have " + str(your_character.level_9_remaining) + " level 9 spellslots available.")
        input("\nPress enter to return to the main menu.\n\n-------- \n\n")
    except:
        input("You need to create a charcter first.\nPress enter to return to main menu.\n\n-------- \n\n")


def use_spell(your_character):
    spell_selection = input("What level spellslot are you using?\n\n-------- \n\n")
    if spell_selection == "1":
        if your_character.level_1_remaining >= 1:
            your_character.level_1_remaining -= 1
            system('clear')
            input("You have " + str(your_character.level_1_remaining) + " level 1 spellslots remaining.\nPress Enter to return to the Main Menu.\n\n-------- \n\n")
            return your_character
        else:
            input("You do not have enough spell slots remaining. You need to rest first!\n Press enter to continue.\n\n-------- \n\n")
    elif spell_selection == "2":
        if your_character.level_2_remaining >= 1:
            your_character.level_2_remaining -= 1
            system('clear')
            input("You have " + str(your_character.level_2_remaining) + " level 2 spellslots remaining.\nPress Enter to return to the Main Menu.\n\n-------- \n\n")
            return your_character
        else:
            system('clear')
            input("You do not have enough spell slots remaining. You need to rest first!\n Press enter to continue.\n\n-------- \n\n")
    elif spell_selection == "3":
        if your_character.level_3_remaining >= 1:
            your_character.level_3_remaining -= 1
            system('clear')
            input("You have " + str(your_character.level_3_remaining) + " level 3 spellslots remaining.\nPress Enter to return to the Main Menu.\n\n-------- \n\n")
            return your_character
        else:
            system('clear')
            input("You do not have enough spell slots remaining. You need to rest first!\n Press enter to continue.\n\n-------- \n\n")
    elif spell_selection == "4":
        if your_character.level_4_remaining >= 1:
            your_character.level_4_remaining -= 1
            system('clear')
            input("You have " + str(your_character.level_4_remaining) + " level 4 spellslots remaining.\nPress Enter to return to the Main Menu.\n\n-------- \n\n")
            return your_character
        else:
            system('clear')
            input("You do not have enough spell slots remaining. You need to rest first!\n Press enter to continue.\n\n-------- \n\n")
    elif spell_selection == "5":
        if your_character.level_5_remaining >= 1:
            your_character.level_5_remaining -= 1
            system('clear')
            input("You have " + str(your_character.level_5_remaining) + " level 5 spellslots remaining.\nPress Enter to return to the Main Menu.\n\n-------- \n\n")
            return your_character
        else:
            system('clear')
            input("You do not have enough spell slots remaining. You need to rest first!\n Press enter to continue.\n\n-------- \n\n")
    elif spell_selection == "6":
        if your_character.level_6_remaining >= 1:
            your_character.level_6_remaining -= 1
            system('clear')
            input("You have " + str(your_character.level_6_remaining) + " level 6 spellslots remaining.\nPress Enter to return to the Main Menu.\n\n-------- \n\n")
            return your_character
        else:
            system('clear')
            input("You do not have enough spell slots remaining. You need to rest first!\n Press enter to continue.\n\n-------- \n\n")
    elif spell_selection == "7":
        if your_character.level_7_remaining >= 1:
            your_character.level_7_remaining -= 1
            system('clear')
            input("You have " + str(your_character.level_7_remaining) + " level 7 spellslots remaining.\nPress Enter to return to the Main Menu.\n\n-------- \n\n")
            return your_character
        else:
            system('clear')
            input("You do not have enough spell slots remaining. You need to rest first!\n Press enter to continue.\n\n-------- \n\n")
    elif spell_selection == "8":
        if your_character.level_8_remaining >= 1:
            your_character.level_8_remaining -= 1
            system('clear')
            input("You have " + str(your_character.level_8_remaining) + " level 8 spellslots remaining.\nPress Enter to return to the Main Menu.\n\n-------- \n\n")
            return your_character
        else:
            system('clear')
            input("You do not have enough spell slots remaining. You need to rest first!\n Press enter to continue.\n\n-------- \n\n")
    elif spell_selection == "9":
        if your_character.level_9_remaining >= 1:
            your_character.level_9_remaining -= 1
            system('clear')
            input("You have " + str(your_character.level_9_remaining) + " level 9 spellslots remaining.\nPress Enter to return to the Main Menu.\n\n-------- \n\n")
            return your_character
        else:
            system('clear')
            input("You do not have enough spell slots remaining. You need to rest first!\nPress enter to continue.\n\n-------- \n\n")

def rest(your_character):
    your_character.level_1_remaining = your_character.level_1_spellslots
    your_character.level_2_remaining = your_character.level_2_spellslots
    your_character.level_3_remaining = your_character.level_3_spellslots
    your_character.level_4_remaining = your_character.level_4_spellslots
    your_character.level_5_remaining = your_character.level_5_spellslots
    your_character.level_6_remaining = your_character.level_6_spellslots
    your_character.level_7_remaining = your_character.level_7_spellslots
    your_character.level_8_remaining = your_character.level_8_spellslots
    your_character.level_9_remaining = your_character.level_9_spellslots
    input("You are all rested, and spellslots have been restored.\nPress enter to continue.\n\n-------- \n\n")
    return your_character


def get_data(your_character):
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
    return data

loaded_data = []

your_character = Full_Caster("Nothing1", 0)

def save_character(your_character):
    data = get_data(your_character)
    with open("your_character_file.csv", 'w') as your_character_file:
        writer = csv.DictWriter(your_character_file, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)

def load_character():
    with open ('your_character_file.csv', 'r') as your_character_file:
        heading = next(your_character_file)
        reader = csv.reader(your_character_file)
        for row in reader:
            loaded_data = row
    if loaded_data[0] == "Wizard":
        your_character = Full_Caster("Wizard", 0)
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
        print(your_character.level)
        print(your_character.dndclass)
        print(loaded_data[0])
        print(your_character.level_1_remaining)
        return your_character
    elif loaded_data[0] == "Paladin":
        your_character = Half_Caster("Paladin", 0)
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
        print(your_character.level)
        print(your_character.dndclass)
        print(your_character.level_1_remaining)
        input("Enter to continue")
        return your_character
    else:
        "You have an error."
