from os import system
from classes import * 

def main_menu_options(main_menu_option):
    print("To quit at any time, please type: quit")
    print("1: Input class selection, and class level.")
    print("2: Check available spellslots")
    print("3: Use a spell")
    print("4: View spell database")
    print("5: Update character spell-list.")
    print("6: Recommend my next learned spell.")
    print("9: Settings.")
    main_menu_option = input("Enter your option: ")
    return main_menu_option

def do_something(character):
    character.spell_slot_one.consume()
    # return character.spell_slot_one.available
    return 42

def main_menu():
    main_menu_selection = ""
    while main_menu_selection != "quit":
        system('clear')
        main_menu_selection = main_menu_options()
        system('clear')
        if main_menu_selection == "1":
            # global character
            # character = get_character()
            input("Character successfully created. Please press enter to return to main menu.")
            main_menu()
        if main_menu_selection == "2":
            get_spells()
            main_menu()
        if main_menu_selection == "3":
            print("This is option 3.")
            break
        if main_menu_selection == "4":
            print("This is option 4.")
            break
        if main_menu_selection == "5":
            print("This is option 5.")
            break
        if main_menu_selection == "6":
            print("This is option 6.")
            break
        if main_menu_selection == "9":
            print("This is option 9.")
            break
        if main_menu_selection == "quit":
            quit()
        else:
            print("Please only input the number you would like to select.")
            input("Press Enter to return to the Main Menu.")

def get_spells(character):
    try:
        print("You have " + str(character.level_1_spellslots) + " level 1 spellslots available.")
        print("You have " + str(character.level_2_spellslots) + " level 2 spellslots available.")
        print("You have " + str(character.level_3_spellslots) + " level 3 spellslots available.")
        print("You have " + str(character.level_4_spellslots) + " level 4 spellslots available.")
        print("You have " + str(character.level_5_spellslots) + " level 5 spellslots available.")
        print("You have " + str(character.level_6_spellslots) + " level 6 spellslots available.")
        print("You have " + str(character.level_7_spellslots) + " level 7 spellslots available.")
        print("You have " + str(character.level_8_spellslots) + " level 8 spellslots available.")
        print("You have " + str(character.level_9_spellslots) + " level 9 spellslots available.")
    except:
        print("you need to create a charcter first")
    input("Press enter to continue.")

