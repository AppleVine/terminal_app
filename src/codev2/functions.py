from os import system
from classes import *

def main_menu_options():
    print("To quit at any time, please type: quit")
    print("1: Input class selection, and class level.")
    print("2: Check available spellslots")
    print("3: Use a spell")
    print("4: rest")
    print("5: View spell database")
    print("6: Update character spell-list.")
    print("7: Recommend my next learned spell.")
    print("9: Settings.")
    main_menu_option = input("Enter your option: ")
    return main_menu_option

def main_menu():
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

