from os import system
from classes import * 


def main_menu_options():
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

def main_menu():
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
                get_paladin_level()
                break
            elif selection == "Wizard":
                get_wizard_level()
                break
            else:
                print("Please only input the number you would like to select.")
                input("Press Enter to return to the Main Menu.")
        if main_menu_selection == "2":
            print("This is option 2.")       
            break 
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