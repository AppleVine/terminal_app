



# Error Handling

```python
def view_spell_database():
    try:
        print(spell_database)
    except NameError:
        input("Spell database has not been created yet.")
```


```python
try:
    your_character = load_character()
except FileNotFoundError:
    input("Save file is not found. Please create a character.\nPress Enter to continue.\n\n-------- \n\n")
main_menu(your_character)
```


```python
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
    except AttributeError:
        input("You need to create a charcter first.\nPress enter to return to main menu.\n\n-------- \n\n")
```

```python
def get_paladin_level():
    input_level = 0
    your_character = None
    while your_character == None:
        try:
            system('clear')
            input_level = input("What level is your Paladin? Please choose from 1-20.\n")
            system('clear')
            int_input = int(input_level)
            if input_level == "quit":
                quit()
            elif int_input == 1:
                return Half_Caster("Paladin", 1)
            elif int_input == 2:
                return Half_Caster("Paladin", 2, 0, 2)
            elif int_input == 3:
                your_character = Half_Caster("Paladin", 3, 0, 3)
                return your_character
            elif int_input == 4:
                your_character = Half_Caster("Paladin", 4, 0, 3)
                return your_character
            elif int_input == 5:
                your_character = Half_Caster("Paladin", 5, 0, 4, 2)
                return your_character
            elif int_input == 6:
                your_character = Half_Caster("Paladin", 6, 0, 4, 2)
                return your_character
            elif int_input == 7:
                your_character = Half_Caster("Paladin", 7, 0, 4, 3)
                return your_character
            elif int_input == 8:
                your_character = Half_Caster("Paladin", 8, 0, 4, 3)
                return your_character
            elif int_input == 9:
                your_character = Half_Caster("Paladin", 9, 0, 4, 3, 2)
                return your_character
            elif int_input == 10:
                your_character = Half_Caster("Paladin", 10, 0, 4, 3, 2)
                return your_character
            elif int_input == 11:
                your_character = Half_Caster("Paladin", 11, 0, 4, 3, 3)
                return your_character
            elif int_input == 12:
                your_character = Half_Caster("Paladin", 12, 0, 4, 3, 3)
                return your_character
            elif int_input == 13:
                your_character = Half_Caster("Paladin", 13, 0, 4, 3, 3, 1)
                return your_character
            elif int_input == 14:
                your_character = Half_Caster("Paladin", 14, 0, 4, 3, 3, 1)
                return your_character
            elif int_input == 15:
                your_character = Half_Caster("Paladin", 15, 0, 4, 3, 3, 2)
                return your_character
            elif int_input == 16:
                your_character = Half_Caster("Paladin", 16, 0, 4, 3, 3, 2)
                return your_character
            elif int_input == 17:
                your_character = Half_Caster("Paladin", 17, 0, 4, 3, 3, 3, 1)
                return your_character
            elif int_input == 18:
                your_character = Half_Caster("Paladin", 18, 0, 4, 3, 3, 3, 1)
                return your_character
            elif int_input == 19:
                your_character = Half_Caster("Paladin", 19, 0, 4, 3, 3, 3, 2)
                return your_character
            elif int_input == 20:
                your_character = Half_Caster("Paladin", 20, 0, 4, 3, 3, 3, 2)
                return your_character
        except ValueError:
            input("That's not a valid response, please only enter a number from 1-20.\nPress Enter to continue.")
```