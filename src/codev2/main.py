from os import system


main_menu_selection = ""
while main_menu_selection != "quit"
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
            print(character.level_1_spellslots)
        elif selection == "Wizard":
            character = get_wizard_level()
            print(character.level_1_spellslots)
        input("Character successfully created. Please press enter to return to main menu.")