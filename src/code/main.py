from functions import *
from classes import * 

character = None

def get_class_level(info):
    if input == "pally":
    
    elif input == "wizard"

main_menu_selection = ""
while main_menu_selection != "quit":
    system('clear')
    main_menu_selection = main_menu_options()
    system('clear')
    if main_menu_selection == "1":
        print("Please enter in your class from the following choices: ")
        selection = input("Paladin \nWizard\n")
        system('clear')
        if selection == "quit":
            quit()
        elif selection == "Paladin":
            character = get_paladin_level()
            # character = get_class_level(selection)
            print(character.level_1_spellslots)
        elif selection == "Wizard":
            character = get_wizard_level()
            # character = get_class_level(selection)
            print(character.level_1_spellslots)
        input("Character successfully created. Please press enter to return to main menu.")
    if main_menu_selection == "2":
        if character == None:
            print("you need a character")
        else
            get_spells(character)
    # "3: Use a spell"
    if main_menu_selection == "3":
        # what level spell was used
        # get input
        # if "one"
            # character.spell_slot_one.consume(1)

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




# // read from file
# {
#     "class": "wizard",
#     "level": 10,
#     # "cantrips": ["spark", "fire"],
#     "freeSpellslots": {
#         1: 2,
#         2: 0,
#         3: 1,
#         4: 2 
#     }
# } = new Wizard(level = 10, one=2, two=0, three=1,four=2)

# # // write to file
# {
#     "class": "wizard",
#     "level": 10,
#     # "cantrips": ["spark", "fire"],
#     "freeSpellslots": {
#         1: 2,
#         2: 0,
#         3: 1,
#         4: 2 
#     }
# }